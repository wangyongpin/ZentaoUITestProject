import unittest
import HTMLTestRunner
import os,time

current_path = os.path.dirname(__file__)
report_path = os.path.join(current_path,'report')
cases_path = os.path.join(current_path,'test_cases')

discover = unittest.defaultTestLoader.discover(start_dir=cases_path,
                                               pattern='*_case.py',
                                               top_level_dir=cases_path
                                                )
main_suit = unittest.TestSuite()
main_suit.addTest( discover )


html_path = os.path.join(report_path,'report_%s.html'%time.strftime('%Y_%m_%d_%H_%M_%S'))
file = open(html_path,'w',encoding='utf-8')
html_runner =  HTMLTestRunner.HTMLTestRunner( stream=file,
                                              title='禅道UI自动化测试项目',
                                              description='由自动化测试完成，包含大部分'
                                            )
html_runner.run(main_suit)
file.close()

