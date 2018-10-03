#include <string.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <elf.h>

#define close_file(fd) close(fd)

struct my_elf_info{
	char e_class;
	char e_data;
	char e_osabi;
	Elf32_Ehdr ehdr_32;
	Elf64_Ehdr ehdr_64;
};

int open_file(char *file_name)
{
	int fd;
	fd = open(file_name, O_RDONLY);
	if (-1 == fd) {
		perror("open: ");
		return -1;
	}

	return fd;
}

int read_log_elf_hdr(int fd, struct my_elf_info *m_info)
{
	int ret;
	unsigned char e_ident[EI_NIDENT];
	Elf32_Ehdr ehdr_32;
	Elf64_Ehdr ehdr_64;
	ret = read(fd, e_ident, sizeof(e_ident));
	if (ret != sizeof(e_ident)) {
		printf("file too small to read common header info\n");
		return -1;
	}

	if (!(e_ident[EI_MAG0] == 0x7f && e_ident[EI_MAG1] == 'E' 
		&& e_ident[EI_MAG2] == 'L' && e_ident[EI_MAG3] == 'F')) {
		printf("file is not eld file\n");
		return -1;
	}

	m_info->e_class = e_ident[EI_CLASS];

	switch (e_ident[EI_CLASS]) {
		case ELFCLASS32: {
			printf("32bit, ");
			memcpy(&m_info->ehdr_32, e_ident, sizeof(e_ident));
			ret = read(fd, &m_info->ehdr_32.e_type, sizeof(Elf32_Ehdr) - sizeof(e_ident));
			if (ret != sizeof(Elf32_Ehdr) - sizeof(e_ident)) {
				printf("32 bit header not sufficient\n");
				return -1;
			}
		}
		break;

		case ELFCLASS64: {
			printf("64bit, ");
			memcpy(&m_info->ehdr_64, e_ident, sizeof(e_ident));
			ret = read(fd, &m_info->ehdr_64.e_type, sizeof(Elf64_Ehdr) - sizeof(e_ident));
			if (ret != sizeof(Elf64_Ehdr) - sizeof(e_ident)) {
				printf("64 bit header not sufficient\n");
				return -1;
			}
			}
		break;

		default:
			printf("elf class is not known\n");
			return -1;
	}

	m_info->e_data = e_ident[EI_DATA];

	switch (e_ident[EI_DATA]) {
		case ELFDATA2LSB: {
			printf("LSB, ");
		}
		break;

		case ELFDATA2MSB: {
			printf("MSB, ");
		}
		break;

		default:
			printf("elf data is not known\n");
			return -1;
	}

	printf("version: %d, ", e_ident[EI_VERSION]);

	m_info->e_osabi = e_ident[EI_OSABI];

	switch (e_ident[EI_OSABI]) {
		case ELFOSABI_NONE: {
			printf("Unix Systen V ABI, ");
		}
		break;

		case ELFOSABI_NETBSD: {
			printf("NEtBSD ABI, ");
		}
		break;	

		case ELFOSABI_GNU: {
			printf("GNU ABI, ");
		}
		break;	

		default:
			printf("unknow/not supported ABI ");
			return -1;
	}


	printf("ABI version: %d, ", e_ident[EI_ABIVERSION]);

	printf("\n");
	return 0;

}

int read_elf_info(char *file_name)
{
	int fd;
	int ret;
	struct my_elf_info m_info;

	fd = open_file(file_name);
	if (-1 == fd) 
		return -1;
	
	ret = read_log_elf_hdr(fd, &m_info);
	if (-1 == ret)
		return -1;

}

int main(int argc, char *argv[])
{
	if (argc < 2) 
		read_elf_info(argv[0]);
	else

		read_elf_info(argv[1]);
}
