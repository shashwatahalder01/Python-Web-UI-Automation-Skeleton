node {
    try{
      def repoInformation = checkout scm
      def GIT_COMMIT_HASH = repoInformation.GIT_COMMIT
      def parallelTestConfiguration = [
      [

        '[Base ]': 'TestCase/base_test.py',
        '[Test1 ]': 'TestCase/test1.py',
        ]
      ]

      def stepList = prepareBuildStages(parallelTestConfiguration)

      for (def groupOfSteps in stepList) {
        parallel groupOfSteps
      }

    } catch(error) {
      echo "The following error occurred: ${error}"
      throw error
    } finally {
      allure([
        includeProperties: false,
        jdk: '',
        properties: [],
        reportBuildPolicy: 'ALWAYS',
        results: [[path: 'target/allure-results']]
      ])
    }
}


def prepareBuildStages(List<Map<String,String>> parallelTestConfiguration) {
  def stepList = []

  println('Preparing builds...')

  for (def parallelConfig in  parallelTestConfiguration) {
    def parallelSteps = prepareParallelSteps(parallelConfig)
    stepList.add(parallelSteps)
  }

  println(stepList)
  println('Finished preparing builds!')

  return stepList
}


def prepareParallelSteps(Map<String, String> parallelStepsConfig) {
  def parallelSteps = [:]
  for (def key in parallelStepsConfig.keySet()) {
    parallelSteps.put(key, prepareOneBuildStage(key, parallelStepsConfig[key]))
  }
  return parallelSteps
}

def prepareOneBuildStage(String name, String file) {
  return {
    stage("Test: ${name}") {
      println("Test: ${name}")
        withCredentials([
            string(credentialsId: 'pwd_jz_su', variable: 'pwd_jz_su'),
            string(credentialsId: 'db_pwd_aws', variable: 'db_pwd_aws'),
            string(credentialsId: 'selenium_grid_16ram', variable: 'selenium_grid_16ram'),
            ]) {
              // Tests go here
              sh """
                python3 -m pytest ${file}.py --alluredir=${WORKSPACE}/allure-results
              """
          }
    }
  }
}