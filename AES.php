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

	function decrypt($str) {
			return $this->opensslDecrypt($str);
	}

	private function opensslDecrypt($str) {
		$decrypted = openssl_decrypt(base64_decode($str), 'AES-128-CBC', $this->key, OPENSSL_RAW_DATA, $this->iv);
		return $decrypted;
	}


  function decryptString($content) {
	  $aes = new MD5('1234567891234567', 128, '0000000000000000');
	  return $aes->decrypt($content);
  }
}

?>
