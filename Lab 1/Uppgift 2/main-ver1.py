def recept(antal):
    bas = {
        "smör, g": 15,
        "ströbröd, msk": 3,
        "ägg, st": 3,
        "strösocker, dl": 3,
        "vaniljsocker, tsk": 2,
        "bakpulver, tsk": 2,
        "vetemjöl, dl": 3,
        "smör, g": 75,
        "vatten, dl": 1

    }

    # Uträkning för hur mycket ingridienser för x antal personer
    faktor = antal / 4

    print("\n")

    print((faktor*antal)*bas)


# Hur många ska kakan räcka till
recept(4)


### Funkar inte ###