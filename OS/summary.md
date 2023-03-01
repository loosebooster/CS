# Linux

* Linux >> Ubuntu
* Linux = 커널
* Ubuntu = Linux 배포판

<br><br>

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
  
<br><br>


**[ 프로세스 관리 ]**  

---

<br>

## fork() 함수
* fork() 함수 실행 시, 실행한 프로세스와 함께 새로운 프로세스 1개 생성
* (생성전)parent process, (생성후)child process

## execve() 함수
* 전혀 다른 프로그램 생성 시 사용; 기존 프로세스를 별도의 프로세스로 변경하는 방식(프로세스 수 동일)

## exit() 함수
* 종료 처리
* _exit() 함수: 내부 상으로는 exit_group() 시스템 콜 호출


<br><br>


**[ 프로세스 스케줄러 ]**  

---

## Context Switch
* 논리 CPU 상에서 동작하는 프로세스가 바뀌는 것
* 프로세스가 어떤 프로그램을 수행 중이더라도 타임 슬라이스를 모두 소비할 경우 발생

## idle 
* 아무것도 하지 않는 특수한 프로세스

## 처리 성능지표
* throughput: 단위시간 당 처리된 일의 양, 높을수록 좋은 성능 | 완료한 프로세스의 수 / 경과시간
* latency: 각각의 처리가 경과된 시간(시작 ~ 종료), 짧을수록 좋음 | 처리 종료시간 - 처리 시작시간

## load balancer
* 여러 개의 논리 CPU에 프로세스를 공평하게 분배해주는 역할

## CPU 상세정보 확인
* ~~grep -c processor /proc/cpuinfo~~
* sysctl -a | grep machdep.cpu   << Mac


---
