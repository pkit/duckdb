import sys
import win32pipe, win32file

if __name__ == '__main__':
    print('Serving \'%s\' from \'%s\'' % (sys.argv[1], sys.argv[2]))
    pipe = win32pipe.CreateNamedPipe(
        sys.argv[2],
        win32pipe.PIPE_ACCESS_OUTBOUND,
        win32pipe.PIPE_TYPE_BYTE | win32pipe.PIPE_READMODE_BYTE | win32pipe.PIPE_WAIT,
        1, 65536, 65536,
        0,
        None)
    try:
        win32pipe.ConnectNamedPipe(pipe, None)
        win32file.WriteFile(pipe, open(sys.argv[1], 'rb').read())
    finally:
        win32file.CloseHandle(pipe)
