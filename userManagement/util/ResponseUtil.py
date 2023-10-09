class ResponseEntity:
    def __init__(self, status=200, body=None):
        self.status = status
        self.body = body

if __name__ == '__main__':
    print(ResponseEntity(body="test").__dict__)     # 딕셔너리로 변경하면 바로 키, 값이 출력됨