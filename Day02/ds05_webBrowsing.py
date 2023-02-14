# 스택활용
import ds04_stack as st
import webbrowser
import time

st.SIZE = 100
st.stack = [None for _ in range(st.SIZE)]
st.top = -1 

if __name__ == '__main__' :
    urls =['www.naver.com','www.daum.net','www.nate.com','www.google.com']

    for url in urls :
        st.push(url)
        webbrowser.open(f'https://{url}')
        print(url,end='-->')
        time.sleep(1)

    print("close")
    print(st.stack)
    time.sleep(5)

    while True :
        url = st.pop()
        if url == None :
            break
        webbrowser.open(f'https://{url}')
        print(url,end='-->')
        time.sleep(1)

    print("reopen close")
    print(st.stack)

    input("Dont close and Stay")