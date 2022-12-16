from router.home import set_home
from utils.convert import convert
from utils.func import preprocess

from dataset.dataloader import Dataset

if __name__ == "__main__":
    set_home()

    ds = Dataset()
    print(f"Before: {ds.df}")

    func = preprocess

    new_ds = []
    for x in ds.df:
        x[0] = convert(x[0], func)
        new_ds.append(x)
    ds.df = new_ds

    print(f"After: {ds.df}")