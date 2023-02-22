# Linux


## OS
* 사용자 모드 <-> 커널 모드
* 커널(kernel): Linux 운영 체제(OS)의 주요 구성 요소, 컴퓨터 하드웨어와 프로세스를 잇는 핵심 인터페이스

## 사용자 모드
[시스템 콜]
* 프로세스 생성, 삭제
* 메모리 확보, 해제
* 프로세스 간 통신(IPC)
* 네트워크
* 파일시스템 다루기
* 파일 다루기(디바이스 접근)

## 시스템 콜 호출의 동작 순서
* 시스템 콜은 CPU의 특수한 명령을 실행해야만 호출
* (사용자모드)시스템 콜 -> (CPU)Interrupt event -> (커널모드)요청내용 확인|처리 -> (사용자모드)시스템콜 처리 종료
* strace : 프로세스가 어떠한 시스템 콜을 호출했는가 확인하는 명령어 <- mac에서 안됨, ktrace로 변경(에러발생)

## 시스템 콜의 wrapper 함수
* wrapper: 시스템 콜을 호출하는 일만 하는 함수, wrapper 함수는 아키텍처별로 존재

## 표준 C 라이브러리
* 프로그램이 어떠한 라이브러리를 링크하고 있는지 확인(ldd /bin/echo)
* otool -L /bin/ls   
    *  /usr/lib/libutil.dylib (compatibility version 1.0.0, current version 1.0.0)
        /usr/lib/libncurses.5.4.dylib (compatibility version 5.4.0, current version 5.4.0)
        /usr/lib/libSystem.B.dylib (compatibility version 1.0.0, current version 1311.120.1)