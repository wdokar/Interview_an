class PostalCode:

    def __init__(self):
        self.a = "78-900"
        self.b = "80-155"

    def split_postal_code(self, a):
        return a.split("-")

    def generate_range(self):
        postalCodeA = self.split_postal_code(self.a)
        postalCodeB = self.split_postal_code(self.b)
        A2 = int(postalCodeA[0])
        A3 = int(postalCodeA[1])
        B2 = int(postalCodeB[0])
        B3 = int(postalCodeB[1])
        my_file = open("output.txt", "w+")

        if A2 > B2:
            print('Sorry wrong value')
            return

        for k in range(A2, B2 + 1):
            if k == A2:
                for x in range(A3, 1000):
                    my_file.write(self.print_code(k, x) + "\n")

                continue

            if k == B2:
                for y in range(0, B3 + 1):
                    my_file.write(self.print_code(k, y) + "\n")

                continue

            for i in range(0, 1000):
                my_file.write(self.print_code(k, i) + "\n")

        my_file.flush()
        my_file.close()

    def print_code(self, a, b):
        if a < 10:
            a = "0" + str(a)

        if b < 10:
            b = "00" + str(b)

        elif b < 100:
            b = "0" + str(b)

        return "%s-%s" % (a, b)


viewScore = PostalCode()
viewScore.generate_range()