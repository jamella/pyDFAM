import coord_extractor, methodcall_extractor
import signal, sys, time, os

def main():

    def signal_handler(signal, frame):
        
        methodcall_extractor.pullLogFile()
        coord_extractor.pullLogFile()

        time.sleep(10)

        methodcall_extractor.writeMethodCall()
        coord_extractor.writeCOORD()
    
        os.popen("rm *.txt")

        sys.exit(1)
    
    coord_extractor.generateLog()

    signal.signal(signal.SIGINT, signal_handler)
    
    while(True):
        pass

main()
