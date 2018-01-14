from src.save_pickle import save_pickle


def main():
    years = range(2009, 2018)
    for year in years:
        print('-----Saving ' + str(year) + '-----')
        print()
        save_pickle(str(year) + '-01-01', str(year + 1) + '-01-01',
                    testing=False, filename='pickle/' + str(year) + '.pkl')
        print()
        print('============================================================')
        print()


if __name__ == '__main__':
    main()