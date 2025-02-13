from utilss.imports import *

while True:
    clear_terminal()
    opt = menu1()
    match opt:
        case 1:
            clear_terminal()
            opt=menuEntrarCamper1()
            match opt:
                case 1:
                    clear_terminal()
                    registrarse()
                    pass
                case 2:
                    clear_terminal()
                    ingresar()
                    pass
                case 3:
                    clear_terminal()
                    retirarse()
                    pass
                case 4:
                    clear_terminal()
                    pass
            pass
        case 2:
            clear_terminal()
            opt=menuTrainer()
            match opt:
                case 1:
                    clear_terminal()
                    calificar()
                    pass
                case 2:
                    clear_terminal()
                    mostrar_horario_trainer()
                    pass
                case 3:
                    clear_terminal()
                    menuTrainer()
                    pass
            pass
        case 3:
            clear_terminal()
            opt = menuCoordinador()
            match opt:
                case 1:
                    clear_terminal()
                    opt = menuCamperCoordinador()
                    match opt:
                        case 1:
                            clear_terminal()
                            registrarse()
                            pass
                        case 2:
                            clear_terminal()
                            ingresar()
                            pass
                        case 3:
                            clear_terminal()
                            retirarse()
                            pass
                    pass
                case 2:
                    clear_terminal()
                    opt = menuAdministrarGrupos()
                    match opt:
                        case 1:
                            clear_terminal()
                            listar_grupos()
                            pass
                        case 2:
                            clear_terminal()
                            crear_grupo()
                        case 3:
                            clear_terminal()
                            actualizar_grupo()
                            pass
                    pass
                case 3:
                    clear_terminal()
                    calificar()
                    pass
        case 4:
            clear_terminal()
            print("\n¡Hasta luego!")
            break
