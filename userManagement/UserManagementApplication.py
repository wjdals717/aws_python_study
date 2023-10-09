def main():
    from userManagement.view.MenuView import MenuView
    while(MenuView.index()):    #staticmethod이기 때문에 생성없이 바로 호출이 가능하다.
        pass

if __name__ == '__main__':
    main()
    print("프로그램이 종료되었습니다.")