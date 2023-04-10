class CracklePop:
    crackle_text = "Crackle"
    pop_text = "Pop"
    crackle_div = 3
    pop_div = 5

    def __init__(self, start, end, crackle_text=None, crackle_div=None, pop_text=None, pop_div=None):
        self.start = start
        self.end = end
        self.crackle_text = CracklePop.crackle_text if crackle_text is None else crackle_text
        self.crackle_div = CracklePop.crackle_div if crackle_div is None else crackle_div
        self.pop_text = CracklePop.pop_text if pop_text is None else pop_text
        self.pop_div = CracklePop.pop_div if pop_div is None else pop_div

    def run(self):
        for num in range(self.start, self.end+1):
            if num % self.crackle_div == 0 and num % self.pop_div == 0:
                print(self.crackle_text + self.pop_text)
            elif num % self.crackle_div == 0:
                print(self.crackle_text)
            elif num % self.pop_div == 0:
                print(self.pop_text)
            else:
                print(num)


def main():
    cp = CracklePop(1, 100)
    cp.run()


if __name__ == "__main__":
    main()
