<?php
class MD5 {
	private $iv;
	private $key;
	private $bit; //Only can use 128, 256
	function __construct($key, $bit = 128, $iv = "") {
		// gen key
			$this->key = hash('MD5', $key, true);
		// gen iv
			$this->iv = hash('MD5', $iv, true);
	}
	function encrypt($str) {
			return $this->opensslEncrypt($str);
	}
	function decrypt($str) {
			return $this->opensslDecrypt($str);
	}
	private function opensslEncrypt($str) {
		$data = openssl_encrypt($str, 'AES-128-CBC', $this->key, OPENSSL_RAW_DATA, $this->iv);
		return base64_encode($data);
	}
	private function opensslDecrypt($str) {
		$decrypted = openssl_decrypt(base64_decode($str), 'AES-128-CBC', $this->key, OPENSSL_RAW_DATA, $this->iv);
		return $decrypted;
	}

  function encryptString($content) {
	  $aes = new MD5('1234567891234567', 128, '0000000000000000');  //key = 1234567891234567(16) / bit = 128 /iv = 0000000000000000(16)
	  return $aes->encrypt($content);
  }

  function decryptString($content) {
	  $aes = new MD5('1234567891234567', 128, '0000000000000000');
	  return $aes->decrypt($content);
  }
}

function changeright($value)
{
	$decrypt = new MD5('1234567891234567', 128, '0000000000000000');
	$decrypt = MD5::decryptString($value);
	// echo "解密後:".$decrypt."<br>";
	return $decrypt;
}

function changeAES($value)
{
	$encrypt = new MD5('1234567891234567', 128, '0000000000000000');
	$encrypt = MD5::encryptString($value);
	// echo "加密後:".$encrypt."<br>";
	return $encrypt;
}

// $str = '111';
// $encrypt = new MD5('1234567891234567', 128, '0000000000000000');
// $decrypt = new MD5('1234567891234567', 128, '0000000000000000');
// $encrypt = MD5::encryptString($str);
// $decrypt = MD5::decryptString($encrypt);
// echo "原始字串:".$str."<br>";
// echo "加密後:".$encrypt."<br>";
// echo "解密後:".$decrypt."<br>";
?>
