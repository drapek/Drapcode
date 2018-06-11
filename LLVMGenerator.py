class LLVMGenerator:
    header_text = ""
    main_text = ""
    reg_iter = 1
    str_decl_iter = 1

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

        self.main_text += f"%{self.reg_iter} = load {var_type}, {var_type}* %{var_id}\n"
        self.reg_iter += 1
        self.main_text += f"%{self.reg_iter} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({var_size}, {var_size}* @str.{self.str_decl_iter-1}, i32 0, i32 0), {var_type} %{self.reg_iter-1})\n"
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

        self.main_text += f"%{self.reg_iter} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ({var_size}, {var_size}* @str.{self.str_decl_iter-1}, i32 0, i32 0), {var_type}* %{var_id})\n"
        self.reg_iter += 1

    def declare(self, var_id, var_type):
        var_type = self.__translate_type_to_llvm(var_type)

        self.main_text += f"%{var_id} = alloca {var_type}\n"

    def assign(self, var_id, value, var_type):
        var_type = self.__translate_type_to_llvm(var_type)

        self.main_text += f"store {var_type} {value}, {var_type}* %{var_id}\n"

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text

    def __translate_type_to_llvm(self, origin_type):
        if origin_type == "double":
            return "double"
        elif origin_type == "int":
            return "i32"
        else:
            raise ValueError("Undefined type in LLVM!")

