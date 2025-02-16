FILEPATH_ERRORS_H = project_path + '/include/errors.h'

header = '''/**
 * @file errors.h
 * @author your name (you@domain.com)
 * @brief 
 * @version 0.1
 * @date 2025-02-08
 * 
 * @copyright Copyright (c) 2025
 * 
 */

/**
 * @brief 
 * 
 */
enum class rapidPluginErrors_t
{
  NO_ERROR = 0,             // No error has occured
  UNKNOWN_ERROR,            // Unknown error is a catch to be used when no other error is applicable
'''

footer = '''} rapidPluginErrors;

'''

custom_errors = '''  // template ERRORS
  TEMPLATE_ERROR1,          // Template error 1
  TEMPLATE_ERROR2,          // Template error 2
  TEMPLATE_ERROR3,          // Template error 3
'''

try:
  open(FILEPATH_ERRORS_H, "r+")
  print(info + '\'errors.h\' already present')
  with open(FILEPATH_ERRORS_H, "r") as f:
    lines = f.readlines()
    if any(custom_errors.split('\n')[1].strip() in line for line in lines):
      print(info + '\'errors.h\' already contains template custom errors')
    else:
      with open(FILEPATH_ERRORS_H, "w") as f_write:
        for line in lines:
          if line.strip() == footer.strip():
        f_write.write(custom_errors)
          f_write.write(line)
      print(info + '\'errors.h\' updated with template custom errors')

except:
  print(warning + '\'errors.h\' not present, generating default...')
  try:
    with open(FILEPATH_ERRORS_H, 'x') as f:
      f.write(header + custom_errors + footer)
  except:
    print(error + '\'errors.h\' could not be written to')