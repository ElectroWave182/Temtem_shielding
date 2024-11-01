from sys import stdin, stdout
input, print = stdin.readline, stdout.write


def entry (type):

    try:
        return type (input ())
    except:
        return entry (type)


def main ():

    while True:

        # Entry taking

        print ("\nFirst phase!\n------------\n\n")

        print ("Enter the attack stat you want to have as a reference...\n")
        atk = entry (int)
        print ('\n')

        print ("Enter the move power you want to have as a reference...\n")
        move = entry (int)
        print ('\n')

        puiss = atk * move
        even = 1

        while True:

            print ("\nSecond phase!\n-------------\n\n")

            even = 1 - even

            print ("Enter the HP base stat you're using...\n(-1 to return to the first phase)\n")
            hp = entry (int)
            print ('\n')
            if hp == -1:
                break

            print ("Enter the " + ("weakest", "strongest")[even] + " defense base stat you're using...\n(-1 to return to the first phase)\n")
            defe = entry (int)
            print ('\n')
            if defe == -1:
                break

            while True:

                print ("\nThird phase!\n------------\n\n")

                print ("Enter the TVs you left for resistance...\n(-1 to return to the second phase)\n")
                tvMax = entry (int)
                print ('\n')
                if tvMax == -1:
                    break


                # Calculating options

                delta = (35 * (17 / (even + 1) * hp + 17 * defe - 300 * even + 1200) + 70 / (even + 1) * tvMax + 25 * puiss) * puiss

                option_a = (17 / 2 * defe + 5 / 14 * puiss + 300 - delta ** 0.5 / 14) * (even + 1) + tvMax
                option_b = (17 / 2 * defe + 5 / 14 * puiss + 300 + delta ** 0.5 / 14) * (even + 1) + tvMax
                option_c = 0
                option_d = min (tvMax, 500)

                options = [option_a, option_b, option_c, option_d]


                # Calculating results

                print ("\nFourth phase!\n-------------\n\n")

                def strokes (tvHp):

                    numerator = (0.2 / (even + 1) * (tvMax - tvHp) + 1.7 * defe + 60) * (0.4 * tvHp + 3.4 * hp + 120)
                    denominator = 2.8 / (even + 1) * (tvMax - tvHp) + 23.8 * defe + puiss + 840

                    return numerator / denominator

                results = [
                    (opt, strokes (opt))
                    for opt in options
                ]
                results.sort (key = lambda x: x[1], reverse = True)


                # Outputing the best one

                for opt, stk in results:
                    if option_c <= opt <= option_d:
                        tvHp = round (opt)
                        break

                tvDefe = tvMax - tvHp
                print ("Your temtem require " + str (tvHp) + " TVs in HP stat and " + str (tvDefe) + " TVs in defense stat" + "s" * even + ".\n\n")


                # Retrying

                print ("Press enter to retry...\n")
                input ()


main ()
