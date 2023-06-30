### GitHub RestAPI 를 이용해서 GitHub Repositery 정보가져오는 프로그램입니다. 

[Github RestAPI Doc](https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#get-a-repository)    
[Github RestAPI 사용제한 doc](https://docs.github.com/ko/apps/creating-github-apps/registering-a-github-app/rate-limits-for-github-apps)  
[AuthToken 발급방법](https://docs.github.com/ko/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens)  
[Github RestAPI AuthToken 사용법](https://docs.github.com/ko/rest/guides/getting-started-with-the-rest-api?apiVersion=2022-11-28)  

https://github.com/settings/apps  

#### 프로그램 실행법  
 1. Github oauth을 발급받고 restapi header 부분에 발급받은 api key 추가.
 2. 찾고싶은 Github Repository 찾기    
 3. python get_info_from_api.py 실행    

#### 출력결과물  

 - Excel 형식(columns = [filename, content])  
 - tree 출력구조의 txt파일  

