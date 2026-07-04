class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        # remove spaces
        s = s.replace(" ", "")

        # helper func to check if character can be converted into integer
        def is_int(c):
            try:
                integer = int(c)
            except ValueError:
                return False
            else:
                return True

        # helper func to split string by +-*/()
        def split_str_into_arr(s):
            cur, arr = "", []
            for i, c in enumerate(s):
                if is_int(c):
                    cur += c
                elif c == "(":
                    arr.append(c)
                elif c in ["+", "-"] and i>0 and s[i-1]=="(":
                    arr.append("0")
                    arr.append(c)
                else:
                    arr.append(cur)
                    cur = ""
                    arr.append(c)
            if cur:
                arr.append(cur)
            return arr
        s = split_str_into_arr(s)

        # evaluate expression when there's no brackets
        def eval_no_brackets(arr):
            res, operator = 0, None
            for a in arr:
                if a in ["+", "-"]:
                    operator = a
                if operator is None:
                    res += a
                else:
                    if is_int(a):
                        res = res + a if operator == "+" else res - a
                    else:
                        operator = a
            return res

        # use stack to deal with () when evaluating strings
        stack = []
        for c in s:
            if c in ["(", "+", "-"]:
                stack.append(c)
            elif is_int(c):
                stack.append(int(c))
            elif c == ")":
                # when encounter ), calc value within current bracket pair
                temp_storage = []
                while stack and stack[-1] != "(":
                    temp_storage.append(stack.pop())
                if stack and stack[-1] == "(":
                    stack.pop()
                stack.append(eval_no_brackets(temp_storage[::-1]))

        return eval_no_brackets(stack)
