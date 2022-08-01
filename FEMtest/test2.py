from time import time


def haha(counts, x):
    for _ in range(int(counts)):
        x[0] = 1
    print('done')


def main():
    a = [0, 0]
    start = time()
    haha(4E8, a)
    end = time()
    print(f'总耗时: {end - start:.3f}秒.')


if __name__ == '__main__':
    main()
