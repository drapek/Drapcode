class LLVMGenerator:
    header_text = ""
    main_text = ""
    reg_iter = 1

    def print(self, var_id):
        # TODO delete commented lines later
        # str_len = len(text)
        # str_type = "[{} x i8]".format(str_len + 2)
        # self.header_text += "@.str{0} = constant{1} c\"{2}\\0A\\00\"\n".format(self.reg_iter, str_type, text)
        self.main_text += f"%{self.reg_iter} = load i32, i32* %{var_id}\n"
        self.reg_iter += 1
        self.main_text += f"%{self.reg_iter} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strp, i32 0, i32 0), i32 %{self.reg_iter-1})\n"
        self.reg_iter += 1

    def scanf(self, var_id):
        self.main_text += f"%{self.reg_iter} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([3 x i8], [3 x i8]* @strs, i32 0, i32 0), i32* %{var_id})\n"
        self.reg_iter += 1

    def declare(self, var_id):
        self.main_text += f"%{var_id} = alloca i32\n"

    def assign(self, var_id, value):
        self.main_text += f"store i32 {value}, i32* %{var_id}\n"

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "@strp = constant [4 x i8] c\"%d\\0A\\00\"\n"
        text += "@strs = constant [3 x i8] c\"%d\\00\"\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text

