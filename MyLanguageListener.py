from tfGrammarListener import tfGrammarListener

class MyCustomListener(tfGrammarListener):
    variables = {}

    def enterAssignment(self, ctx):
        var_name = ctx.ID().getText()
        expr_value = self.evaluate_expr(ctx.expr())
        self.variables[var_name] = expr_value
        # print(f"IR: {var_name} = {expr_value}")
        
        var_name_txt = ctx.ID().getText()
        expr_value_txt = ctx.expr().getText()
        print(f"IR: {var_name_txt} = {expr_value_txt}")

    def enterIf_statement(self, ctx):
        condition = ctx.expr().getText()
        print(f"IR: if {condition} then")

    def exitIf_statement(self, ctx):
        print("IR: end")

    def evaluate_expr(self, ctx):
        if ctx.INT():
            return int(ctx.INT().getText())
        elif ctx.ID():
            var_name = ctx.ID().getText()
            return self.variables.get(var_name, 0)
        elif ctx.op:
            op = ctx.op.text
            left_operand = self.evaluate_expr(ctx.expr(0))
            right_operand = self.evaluate_expr(ctx.expr(1))
            if op == '+':
                return left_operand + right_operand
            elif op == '-':
                return left_operand - right_operand
            elif op == '*':
                return left_operand * right_operand
            elif op == '/':
                return left_operand / right_operand
        elif ctx.getChildCount() == 3:
            return self.evaluate_expr(ctx.expr(0))
