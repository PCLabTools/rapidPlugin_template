FILEPATH_ERRORS_H = project_path + '/include/errors.h'

contents = '''/**
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
  NO_ERROR = 0,
  UNKNOWN_ERROR
}

'''

try:
  open(FILEPATH_ERRORS_H, "r+")
  print(info + '\'errors.h\' already present')
except:
  print(warning + '\'errors.h\' not present, generating default...')
  try:
    with open(FILEPATH_ERRORS_H, 'x') as f:
      f.write(contents)
  except:
    print(error + '\'errors.h\' could not be written to')