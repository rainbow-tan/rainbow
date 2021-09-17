### 1、场景：

使用Python处理业务时，往往会调用到其他接口，比如调用WebService，调用HTTP接口，也会连接数据库，连接Redis等，这些场景都会由于网络原因、并发数量过大、用户名密码错误等问题，导致调用失败，程序抛出异常。此时我们需要进行retry处理。

### 2、一般retry写法

一般retry写法，使用while或者for循环，贴个伪代码看看即可，这种大家都能写出来。

<img src="/Users/tiger/Library/Application Support/typora-user-images/image-20210907194821772.png" alt="image-20210907194821772" style="zoom:50%;" />

### 3、推荐使用第三方库tenacity中的retry装饰器

使用第三方库tenacity中的retry装饰器来实现重试，这个retry装饰器比较通用，复用性比较好，也能根据多种场景来判断是否重试。

- #### 安装

  pypi链接

  https://pypi.org/project/tenacity/

  安装命令

  ```python
  python -m pip install tenacity
  ```

- #### 函数中抛出异常就会重试,一直重试到没有异常抛出

```python
import random

from tenacity import retry  # 导入retry装饰器


@retry  # 函数中抛出异常就会重试,一直重试到没有异常抛出
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 5
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise Exception(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)
    return number


if __name__ == '__main__':
    ret = test_retry('name', 23)
    print(f'ret:{ret}')
```

- #### 函数中抛出异常就会重试,一直重试到没有异常抛出,重试前会等wait秒

```python
import random

from tenacity import *


@retry(wait=wait_fixed(2))  # 函数中抛出异常就会重试,一直重试到没有异常抛出,重试前会等wait秒
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 5
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise Exception(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)
    return number


if __name__ == '__main__':
    now = time.time()
    ret = test_retry('name', 23)
    print(f'ret:{ret}')
    end = time.time()
    print(f'用时:{end - now}秒')
```

- #### 函数中抛出异常就会重试,重试stop次就不重试了,重试失败，会抛出异常

```python
   import random
   
   from tenacity import *
   
   
   @retry(stop=stop_after_attempt(2))
   # 函数中抛出异常就会重试,重试stop次就不重试了,重试失败，会抛出异常
   def test_retry(name, age):
       """
       假装有参数,一个是name姓名,一个是age年龄
       随机一个0-10的数,随机数小于max_number就抛出异常
       :param name:姓名
       :param age:年龄
       :return:随机数
       """
       number = random.randint(0, 10)
       max_number = 5
       if number < max_number:
           msg = f'随机数字小于:{max_number}, 随机数:{number}'
           print(msg)
           raise Exception(msg)
       else:
           msg = f'随机数不小于:{max_number}, 随机数:{number}'
           print(msg)
       return number
   
   
   if __name__ == '__main__':
       try:
           ret = test_retry('name', 23)
           print(f'ret:{ret}')
       except Exception as e:
           print(f'重试次数用完后,捕获到的异常:{e}')
           pass
```

- #### 函数中抛出异常就会重试,重试stop秒就不重试了,重试失败，会抛出异常

```python
import random

from tenacity import *


@retry(stop=stop_after_delay(2))
# 函数中抛出异常就会重试,重试stop秒就不重试了,重试失败，会抛出异常
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 5
    time.sleep(2)
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise Exception(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)

    return number


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'重试时间超时后,捕获到的异常:{e}')
        pass
```

- #### 函数中抛出异常就会重试,重试stop秒后或重试stop次后就不重试了,重试失败，会抛出异常

```python
import random

from tenacity import *


@retry(stop=(stop_after_delay(4) | stop_after_attempt(2)))
# 函数中抛出异常就会重试,重试stop秒后或重试stop次后就不重试了,重试失败，会抛出异常
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 7
    time.sleep(2)
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise Exception(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)

    return number


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'重试时间超时或次数超过后,捕获到的异常:{e}')
        pass
```

- #### 根据捕获到的异常类型判断是否需要retry

```python
import random

from tenacity import *


@retry(retry=retry_if_exception_type(IOError))
# 函数中抛出异常且异常类型是retry类型就会重试,其他类型会抛出异常
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 7
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        if random.randint(0, 1):
            print('不应该被捕获到,会进入retry逻辑')
            raise IOError(msg)  # 测试抛出不同类型的异常,是否会进入retry逻辑,
        else:
            print('应该被捕获到,不会进入retry逻辑')
            raise Exception('Exception msg')  # 测试抛出不同类型的异常,是否会进入retry逻辑
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)

    return number


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'捕获到的异常信息:{e}')
        print(f'捕获到的异常类型:{type(e)}')
        pass
```

- #### 解析返回值来决定是否需要retry

```python
import random

from tenacity import *


def check_return_info(return_info):
    # 检查函数的返回值
    if return_info == 1:
        return True  # 返回True会触发retry
    else:
        return False  # 返回False不会触发retry


@retry(retry=retry_if_result(check_return_info))
# 函数返回值进入check_return_info函数检查，如果check_return_info函数返回True则retry,否则不retry
# 一般用于函数中不会抛异常的情况,直接根据返回值来判断是否需要retry
# 如果函数中抛出异常,也不会进入retry,直接会抛出异常,因为抛出了异常,就无法触发return语句，也就进不去check_return_info函数,也就不会retry
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 7
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        # raise Exception(msg)
        return 1
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)
        return 0


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'捕获到的异常信息:{e}')
        print(f'捕获到的异常类型:{type(e)}')
        pass
```

- #### 抛出原来的异常信息(重试失败后，默认抛出RetryError)

```python
import random

from tenacity import *


@retry(stop=stop_after_attempt(2), reraise=True)
# 函数中抛出异常就会重试,重试stop次就不重试了,此时失败，会抛出异常
# 当出现异常后，tenacity 会进行重试，若重试后还是失败，默认情况下，往上抛出的异常会变成 RetryError，而不是最根本的原因。
# 因此可以加一个参数（reraise=True),使得当重试失败后，往外抛出的异常还是原来的那个。
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 5
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise Exception(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)
    return number


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'重试次数用完后,捕获到的异常:{e}')
        pass
```

- #### 重试失败后的回调函数

```python
import random

from tenacity import *


def callback(return_object):
    print(f'return_object:{return_object}')
    print(f'return_object type:{type(return_object)}')
    print('我是回调函数哟')
    print(vars(return_object))


@retry(stop=stop_after_attempt(1), reraise=True, retry_error_callback=callback)
# 函数中抛出异常就会重试,重试stop次就不重试了,此时失败，会抛出异常
# retry依旧失败后,执行回调函数callback
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 5
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise Exception(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)
    return number


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'重试次数用完后,捕获到的异常:{e}')
        pass
```

- #### 以上的用法可以合在一起使用，例如

```python
import random

from tenacity import *


@retry(stop=(stop_after_attempt(2) or stop_after_delay(2)), retry=retry_if_exception_type(IOError), wait=wait_fixed(2),
       reraise=True)
# 函数中抛出异常就会重试,重试stop次就不重试了,此时失败，会抛出异常
# 函数中抛出异常就会重试,重试stop秒就不重试了,此时失败，会抛出异常
# 函数中抛出异常且异常类型是retry类型就会重试,其他类型会抛出异常
# 重试中等待wait秒
# 当出现异常后，tenacity 会进行重试，若重试后还是失败，默认情况下，往上抛出的异常会变成 RetryError，而不是最根本的原因。
# 因此可以加一个参数（reraise=True),使得当重试失败后，往外抛出的异常还是原来的那个。
def test_retry(name, age):
    """
    假装有参数,一个是name姓名,一个是age年龄
    随机一个0-10的数,随机数小于max_number就抛出异常
    :param name:姓名
    :param age:年龄
    :return:随机数
    """
    number = random.randint(0, 10)
    max_number = 8
    if number < max_number:
        msg = f'随机数字小于:{max_number}, 随机数:{number}'
        print(msg)
        raise IOError(msg)
    else:
        msg = f'随机数不小于:{max_number}, 随机数:{number}'
        print(msg)
    return number


if __name__ == '__main__':
    try:
        ret = test_retry('name', 23)
        print(f'ret:{ret}')
    except Exception as e:
        print(f'重试次数用完后,捕获到的异常:{e}')
        pass
```

***学习链接:***https://iswbm.com/99.html

