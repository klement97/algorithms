class HashTable:

    def __init__(self, size=None, fill_up_ratio=None):
        self.__init_size(size)
        self.__init_fill_up_ratio(fill_up_ratio)
        self.__init_buckets()
        self.__allocated_size = 0

    def __str__(self):
        return {
            key: value
            for bucket in self.buckets
            for key, value in bucket
        }

    def __repr__(self):
        _repr = {
            key: value
            for bucket in self.buckets
            for key, value in bucket
        }
        return str(_repr)

    def __init_size(self, size):
        if size and size <= 0:
            raise ValueError(f'Size can not be less than 1. Given size is {size}')

        self.size = size or 10

    def __init_fill_up_ratio(self, fill_up_ratio):
        if fill_up_ratio and fill_up_ratio <= 0:
            raise ValueError(f'Fill up ratio can not be less or equal to zero.'
                             f'{fill_up_ratio=}')

        self.fill_up_ratio = 2 / 3

    def __init_buckets(self):
        self.buckets = []
        for _ in range(self.size):
            self.buckets.append([])

    @staticmethod
    def __raise_key_error(key):
        raise KeyError(f'Requested key was not found inside the HashTable.'
                       f' {key=}')

    def __get_index(self, key) -> int:
        return hash(key) % self.size

    def __get_bucket(self, key) -> list:
        index = self.__get_index(key)
        return self.buckets[index]

    @staticmethod
    def __get_bucket_index(key, bucket: list[tuple]) -> int:
        for i, (k, _) in enumerate(bucket):
            if key == k:
                return i

    def __is_almost_full(self) -> bool:
        return self.__allocated_size > int(self.size * self.fill_up_ratio)

    def __double_size(self):
        for _ in range(self.size):
            self.buckets.append([])

        self.size = self.size * 2

    def get(self, key):
        bucket = self.__get_bucket(key)
        for k, v in bucket:
            if k == key:
                return v

        self.__raise_key_error(key)

    def set(self, key, value):
        bucket = self.__get_bucket(key)
        if not bucket:
            self.__allocated_size += 1
            if self.__is_almost_full():
                self.__double_size()

        bucket_index = self.__get_bucket_index(key, bucket)
        if bucket_index is not None:
            bucket[bucket_index] = (key, value)
        else:
            bucket.append((key, value))

    def delete(self, key):
        bucket = self.__get_bucket(key)
        bucket_index = self.__get_bucket_index(key, bucket)
        if bucket_index is None:
            self.__raise_key_error(key)

        del bucket[bucket_index]
