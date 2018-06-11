class LLVMGenerator:
    header_text = ""
    main_text = ""
    reg_iter = 1

    def print(self, text):
        str_len = len(text)
        str_type = "[{} x i8]".format(str_len + 2)
        self.header_text += "@.str{0} = constant{1} c\"{2}\\0A\\00\"\n".format(self.reg_iter, str_type, text)
        self.main_text += "%{} = load i32, i32* %{}\n".format(self.reg_iter, text)
        self.reg_iter += 1
        self.main_text += "%{} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ({}, {}* @.str{}, i32 0, i32 0), i32 %{})\n".\
            format(self.reg_iter, str_type, str_type, self.reg_iter-1, self.reg_iter-1)
        self.reg_iter += 1

    def generate(self):
        text = "declare i32 @printf(i8*, ...)\n"
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 0 }\n"
        return text

