# test_decimal_to_binary.py
import pytest
from decimal_to_binary import decimal_to_binary

def test_decimal_to_binary():
    assert decimal_to_binary(10) == '1010'
    assert decimal_to_binary(20) == '10100'
    assert decimal_to_binary(30) == '11110'
    assert decimal_to_binary(0) == '0'

def test_decimal_to_binary_negative():
    with pytest.raises(ValueError):
        decimal_to_binary(-10)

def test_decimal_to_binary_non_integer():
    with pytest.raises(TypeError):
        decimal_to_binary(10.5)
```

```javascript
// decimalToBinary.test.js
import { decimalToBinary } from './decimalToBinary';

describe('decimalToBinary', () => {
  it('should convert decimal to binary', () => {
    expect(decimalToBinary(10)).toBe('1010');
    expect(decimalToBinary(20)).toBe('10100');
    expect(decimalToBinary(30)).toBe('11110');
    expect(decimalToBinary(0)).toBe('0');
  });

  it('should throw error for negative decimal', () => {
    expect(() => decimalToBinary(-10)).toThrowError();
  });

  it('should throw error for non-integer decimal', () => {
    expect(() => decimalToBinary(10.5)).toThrowError();
  });
});
