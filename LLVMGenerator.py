class LLVMGenerator:
    header_text = ""
    main_buffer = ""
    buffer = ""
    block_stack = []
    reg_iter = 1
    global_iter_tmp = 1
    str_decl_iter = 1
    block_iter = 1

    #################
    # IO operations #
    #################
    def print(self, var_id, var_type):
        var_type = self.__translate_type_to_llvm(var_type)

        # declare strings which will be the output
        string_declaration = ""
        if var_type == "i32":
            var_size = "[4 x i8]"
            string_declaration = f"@str.{self.str_decl_iter} = constant {var_size} c\"%d\\0A\\00\"\n"
        elif var_type == "double":
            var_size = "[4 x i8]"
            string_declaration = f"@str.{self.str_decl_iter} = constant {var_size} c\"%f\\0A\\00\"\n"
        self.str_decl_iter += 1
        self.header_text += string_declaration

        self.buffer += f"%{self.reg_iter} = load {var_type}, {var_type}* %{var_id}\n"
        self.reg_iter += 1
        self.buffer += f"%{self.reg_iter} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({var_size}, {var_size}* @str.{self.str_decl_iter-1}, i32 0, i32 0), {var_type} %{self.reg_iter-1})\n"
        self.reg_iter += 1

    def scanf(self, var_id, var_type):
        var_type = self.__translate_type_to_llvm(var_type)

        # declare strings which will be the output
        string_declaration = ""
        if var_type == "i32":
            var_size = "[3 x i8]"
            string_declaration = f"@str.{self.str_decl_iter} = constant {var_size} c\"%d\\00\"\n"
        elif var_type == "double":
            var_size = "[4 x i8]"
            string_declaration = f"@str.{self.str_decl_iter} = constant {var_size} c\"%lf\\00\"\n"
        self.str_decl_iter += 1
        self.header_text += string_declaration

        self.buffer += f"%{self.reg_iter} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ({var_size}, {var_size}* @str.{self.str_decl_iter-1}, i32 0, i32 0), {var_type}* %{var_id})\n"
        self.reg_iter += 1

    def declare(self, var_id, var_type):
        var_type = self.__translate_type_to_llvm(var_type)

        self.buffer += f"%{var_id} = alloca {var_type}\n"

    def assign(self, var_id, value, var_type):
        var_type = self.__translate_type_to_llvm(var_type)

        self.buffer += f"store {var_type} {value}, {var_type}* %{var_id}\n"

    def load_int(self, var_id):
        self.buffer += f"%{self.reg_iter} = load i32, i32* %{var_id}\n"
        self.reg_iter += 1

    def load_double(self, var_id):
        self.buffer += f"%{self.reg_iter} = load double, double* %{var_id}\n"
        self.reg_iter += 1

    ####################
    # Math operations #
    ###################
    def add_int(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = add i32 {val1}, {val2}\n"
        self.reg_iter += 1

    def add_double(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = fadd double {val1}, {val2}\n"
        self.reg_iter += 1

    def sub_int(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = sub i32 {val1}, {val2}\n"
        self.reg_iter += 1

    def sub_double(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = fsub double {val1}, {val2}\n"
        self.reg_iter += 1

    def mult_int(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = mul i32 {val1}, {val2}\n"
        self.reg_iter += 1

    def mult_double(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = fmul double {val1}, {val2}\n"
        self.reg_iter += 1

    def div_int(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = sdiv i32 {val1}, {val2}\n"
        self.reg_iter += 1

    def div_double(self, val1, val2):
        self.buffer += f"%{self.reg_iter} = fdiv double {val1}, {val2}\n"
        self.reg_iter += 1

    ##########################
    # conditional statements #
    ##########################
    def if_start(self):
        self.buffer += f"br i1 %{self.reg_iter - 1}, label %true{self.block_iter}, label %false{self.block_iter}\n"
        self.buffer += f"true{self.block_iter}:\n"
        self.block_stack.append(self.block_iter)
        self.block_iter += 1

    def if_end(self):
        block_nmb = self.block_stack.pop()
        self.buffer += f"br label %false{block_nmb}\n"
        self.buffer += f"false{block_nmb}:\n"

    def while_start(self):
        self.buffer += f"br label %while{self.block_iter}\n"
        self.buffer += f"while{self.block_iter}:\n"

        self.buffer += f"br i1 %{self.reg_iter - 1}, label %true{self.block_iter}, label %false{self.block_iter}\n"
        self.buffer += f"true{self.block_iter}:\n"
        self.block_stack.append(self.block_iter)
        self.block_iter += 1

    def while_end(self):
        block_nmb = self.block_stack.pop()
        self.buffer += f"br label %while{block_nmb}\n"
        self.buffer += f"false{block_nmb}:\n"

    def icmp(self, val1, val2):
        """ val1 and val2 should be value eg. 4.0 or register number eg. %3"""
        self.buffer += f"%{self.reg_iter} = icmp eq i32 {val1}, {val2}\n"
        self.reg_iter += 1

    def func_start(self, func_name,):
        self.main_buffer += self.buffer
        self.global_iter_tmp = self.reg_iter
        self.buffer = f"define i32 @{func_name}() nounwind {{\n"
        self.reg_iter = 1

    def func_end(self):
        self.buffer += f"ret i32 %{self.reg_iter - 1}\n"
        self.buffer += "}\n"
        self.header_text += self.buffer
        self.buffer = ""
        self.reg_iter = self.global_iter_tmp

    def func_call(self, func_name):
        self.buffer += f"%{self.reg_iter} = call i32 @{func_name}()\n"
        self.reg_iter += 1

    #####################
    # Summary generator #
    #####################
    def generate(self):
        self.main_buffer += self.buffer

        text = "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_buffer
        text += "ret i32 0 }\n"
        return text

    def __translate_type_to_llvm(self, origin_type):
        if origin_type == "double":
            return "double"
        elif origin_type == "int":
            return "i32"
        else:
            raise ValueError("Undefined type in LLVM!")
