# DB2ADMIN.WRKSALARYWAGEDEDUCTION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 139
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `EMPLOYEECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 163958

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 3 | `PAYELEMENTSLN300DESP` | VARCHAR(200) |  |  |  |  |
| 4 | `PAYELEMENTSLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 5 | `PAYELEMENTHLN300DESP` | VARCHAR(200) |  |  |  |  |
| 6 | `PAYELEMENTHLN301DESP` | VARCHAR(200) |  |  |  |  |
| 7 | `PAYELEMENTHLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 8 | `PAYELEMENTHLN301AMT` | DECIMAL(11,4) |  |  |  |  |
| 9 | `PAYELEMENTBGD300DESP` | VARCHAR(200) |  |  |  |  |
| 10 | `PAYELEMENTBGD300AMT` | DECIMAL(11,4) |  |  |  |  |
| 11 | `PAYELEMENTSHL300DESP` | VARCHAR(200) |  |  |  |  |
| 12 | `PAYELEMENTSHL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 13 | `PAYELEMENTRO100DESP` | VARCHAR(200) |  |  |  |  |
| 14 | `PAYELEMENTREC300DESP` | VARCHAR(200) |  |  |  |  |
| 15 | `PAYELEMENTRO100AMT` | DECIMAL(11,4) |  |  |  |  |
| 16 | `PAYELEMENTREC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 17 | `PAYELEMENTNSI600DESP` | VARCHAR(200) |  |  |  |  |
| 18 | `PAYELEMENTNSI600AMT` | DECIMAL(11,4) |  |  |  |  |
| 19 | `PAYELEMENTPF101DESP` | VARCHAR(200) |  |  |  |  |
| 20 | `PAYELEMENTPF101AMT` | DECIMAL(11,4) |  |  |  |  |
| 21 | `PAYELEMENTPF102DESP` | VARCHAR(200) |  |  |  |  |
| 22 | `PAYELEMENTPF103DESP` | VARCHAR(200) |  |  |  |  |
| 23 | `PAYELEMENTPF104DESP` | VARCHAR(200) |  |  |  |  |
| 24 | `PAYELEMENTPF102AMT` | DECIMAL(11,4) |  |  |  |  |
| 25 | `PAYELEMENTPF103AMT` | DECIMAL(11,4) |  |  |  |  |
| 26 | `PAYELEMENTPF104AMT` | DECIMAL(11,4) |  |  |  |  |
| 27 | `PAYELEMENTESI101DESP` | VARCHAR(200) |  |  |  |  |
| 28 | `PAYELEMENTESI102DESP` | VARCHAR(200) |  |  |  |  |
| 29 | `PAYELEMENTESI101AMT` | DECIMAL(11,4) |  |  |  |  |
| 30 | `PAYELEMENTESI102AMT` | DECIMAL(11,4) |  |  |  |  |
| 31 | `PAYELEMENTRST300DESP` | VARCHAR(200) |  |  |  |  |
| 32 | `PAYELEMENTRST300AMT` | DECIMAL(11,4) |  |  |  |  |
| 33 | `PAYELEMENTPT300DESP` | VARCHAR(200) |  |  |  |  |
| 34 | `PAYELEMENTPT300AMT` | DECIMAL(11,4) |  |  |  |  |
| 35 | `PAYELEMENTET300DESP` | VARCHAR(200) |  |  |  |  |
| 36 | `PAYELEMENTET300AMT` | DECIMAL(11,4) |  |  |  |  |
| 37 | `PAYELEMENTLWF300DESP` | VARCHAR(200) |  |  |  |  |
| 38 | `PAYELEMENTLWF300AMT` | DECIMAL(11,4) |  |  |  |  |
| 39 | `PAYELEMENTADV300DESP` | VARCHAR(200) |  |  |  |  |
| 40 | `PAYELEMENTADV300AMT` | DECIMAL(11,4) |  |  |  |  |
| 41 | `PAYELEMENTHRD300DESP` | VARCHAR(200) |  |  |  |  |
| 42 | `PAYELEMENTHRD300AMT` | DECIMAL(11,4) |  |  |  |  |
| 43 | `PAYELEMENTELC300DESP` | VARCHAR(200) |  |  |  |  |
| 44 | `PAYELEMENTELC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 45 | `PAYELEMENTLIC300DESP` | VARCHAR(200) |  |  |  |  |
| 46 | `PAYELEMENTLIC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 47 | `PAYELEMENTGLI300AMT` | DECIMAL(11,4) |  |  |  |  |
| 48 | `PAYELEMENTGLI300DESP` | VARCHAR(200) |  |  |  |  |
| 49 | `PAYELEMENTGLN300DESP` | VARCHAR(200) |  |  |  |  |
| 50 | `PAYELEMENTGLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 51 | `PAYELEMENTCLB300DESP` | VARCHAR(200) |  |  |  |  |
| 52 | `PAYELEMENTCLB300AMT` | DECIMAL(11,4) |  |  |  |  |
| 53 | `PAYELEMENTGLN301DESP` | VARCHAR(200) |  |  |  |  |
| 54 | `PAYELEMENTGLN301AMT` | DECIMAL(11,4) |  |  |  |  |
| 55 | `PAYELEMENTLCL300DESP` | VARCHAR(200) |  |  |  |  |
| 56 | `PAYELEMENTLCL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 57 | `PAYELEMENTFLN300DESP` | VARCHAR(200) |  |  |  |  |
| 58 | `PAYELEMENTFLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 59 | `PAYELEMENTTLN300DESP` | VARCHAR(200) |  |  |  |  |
| 60 | `PAYELEMENTTLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 61 | `PAYELEMENTCLN300DESP` | VARCHAR(200) |  |  |  |  |
| 62 | `PAYELEMENTCML300DESP` | VARCHAR(200) |  |  |  |  |
| 63 | `PAYELEMENTCLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 64 | `PAYELEMENTCML300AMT` | DECIMAL(11,4) |  |  |  |  |
| 65 | `PAYELEMENTGSL300DESP` | VARCHAR(200) |  |  |  |  |
| 66 | `PAYELEMENTGTI300DESP` | VARCHAR(200) |  |  |  |  |
| 67 | `PAYELEMENTGSL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 68 | `PAYELEMENTGTI300AMT` | DECIMAL(11,4) |  |  |  |  |
| 69 | `PAYELEMENTMED300DESP` | VARCHAR(200) |  |  |  |  |
| 70 | `PAYELEMENTMED300AMT` | DECIMAL(11,4) |  |  |  |  |
| 71 | `PAYELEMENTIMP300DESP` | VARCHAR(200) |  |  |  |  |
| 72 | `PAYELEMENTIMP300AMT` | DECIMAL(11,4) |  |  |  |  |
| 73 | `PAYELEMENTPTC300DESP` | VARCHAR(200) |  |  |  |  |
| 74 | `PAYELEMENTPTC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 75 | `PAYELEMENTMES300DESP` | VARCHAR(200) |  |  |  |  |
| 76 | `PAYELEMENTMES300AMT` | DECIMAL(11,4) |  |  |  |  |
| 77 | `PAYELEMENTSEC300DESP` | VARCHAR(200) |  |  |  |  |
| 78 | `PAYELEMENTSEC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 79 | `PAYELEMENTCOR300DESP` | VARCHAR(200) |  |  |  |  |
| 80 | `PAYELEMENTCYL300DESP` | VARCHAR(200) |  |  |  |  |
| 81 | `PAYELEMENTCOR300AMT` | DECIMAL(11,4) |  |  |  |  |
| 82 | `PAYELEMENTCYL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 83 | `PAYELEMENTTPT300DESP` | VARCHAR(200) |  |  |  |  |
| 84 | `PAYELEMENTTVL300DESP` | VARCHAR(200) |  |  |  |  |
| 85 | `PAYELEMENTULN300DESP` | VARCHAR(200) |  |  |  |  |
| 86 | `PAYELEMENTVLN300DESP` | VARCHAR(200) |  |  |  |  |
| 87 | `PAYELEMENTTPT300AMT` | DECIMAL(11,4) |  |  |  |  |
| 88 | `PAYELEMENTTVL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 89 | `PAYELEMENTULN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 90 | `PAYELEMENTVLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 91 | `PAYELEMENTMDF300DESP` | VARCHAR(200) |  |  |  |  |
| 92 | `PAYELEMENTMDF300AMT` | DECIMAL(11,4) |  |  |  |  |
| 93 | `PAYELEMENTLDC300DESP` | VARCHAR(200) |  |  |  |  |
| 94 | `PAYELEMENTLDC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 95 | `PAYELEMENTCBL300DESP` | VARCHAR(200) |  |  |  |  |
| 96 | `PAYELEMENTCBL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 97 | `PAYELEMENTAFD300DESP` | VARCHAR(200) |  |  |  |  |
| 98 | `PAYELEMENTAPC300DESP` | VARCHAR(200) |  |  |  |  |
| 99 | `PAYELEMENTAFD300AMT` | DECIMAL(11,4) |  |  |  |  |
| 100 | `PAYELEMENTAPC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 101 | `PAYELEMENTWC300DESP` | VARCHAR(200) |  |  |  |  |
| 102 | `PAYELEMENTWLN300DESP` | VARCHAR(200) |  |  |  |  |
| 103 | `PAYELEMENTWC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 104 | `PAYELEMENTWLN300AMT` | DECIMAL(11,4) |  |  |  |  |
| 105 | `PAYELEMENTOD300DESP` | VARCHAR(200) |  |  |  |  |
| 106 | `PAYELEMENTOCL300DESP` | VARCHAR(200) |  |  |  |  |
| 107 | `PAYELEMENTOD300AMT` | DECIMAL(11,4) |  |  |  |  |
| 108 | `PAYELEMENTOCL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 109 | `PAYELEMENTCON300DESP` | VARCHAR(200) |  |  |  |  |
| 110 | `PAYELEMENTCON300AMT` | DECIMAL(11,4) |  |  |  |  |
| 111 | `PAYELEMENTLIC301DESP` | VARCHAR(200) |  |  |  |  |
| 112 | `PAYELEMENTLIC301AMT` | DECIMAL(11,4) |  |  |  |  |
| 113 | `PAYELEMENTLIC302DESP` | VARCHAR(200) |  |  |  |  |
| 114 | `PAYELEMENTLIC302AMT` | DECIMAL(11,4) |  |  |  |  |
| 115 | `PAYELEMENTLIC303DESP` | VARCHAR(200) |  |  |  |  |
| 116 | `PAYELEMENTLIC303AMT` | DECIMAL(11,4) |  |  |  |  |
| 117 | `PAYELEMENTLIC304DESP` | VARCHAR(200) |  |  |  |  |
| 118 | `PAYELEMENTLIC304AMT` | DECIMAL(11,4) |  |  |  |  |
| 119 | `PAYELEMENTLIC305DESP` | VARCHAR(200) |  |  |  |  |
| 120 | `PAYELEMENTLNR300DESP` | VARCHAR(200) |  |  |  |  |
| 121 | `PAYELEMENTLTL300DESP` | VARCHAR(200) |  |  |  |  |
| 122 | `PAYELEMENTLIC305AMT` | DECIMAL(11,4) |  |  |  |  |
| 123 | `PAYELEMENTLNR300AMT` | DECIMAL(11,4) |  |  |  |  |
| 124 | `PAYELEMENTLTL300AMT` | DECIMAL(11,4) |  |  |  |  |
| 125 | `PAYELEMENTIT100DESP` | VARCHAR(200) |  |  |  |  |
| 126 | `PAYELEMENTIT101DESP` | VARCHAR(200) |  |  |  |  |
| 127 | `PAYELEMENTIT102DESP` | VARCHAR(200) |  |  |  |  |
| 128 | `PAYELEMENTIT103DESP` | VARCHAR(200) |  |  |  |  |
| 129 | `PAYELEMENTIT104DESP` | VARCHAR(200) |  |  |  |  |
| 130 | `PAYELEMENTIT100AMT` | DECIMAL(11,4) |  |  |  |  |
| 131 | `PAYELEMENTIT101AMT` | DECIMAL(11,4) |  |  |  |  |
| 132 | `PAYELEMENTIT102AMT` | DECIMAL(11,4) |  |  |  |  |
| 133 | `PAYELEMENTIT103AMT` | DECIMAL(11,4) |  |  |  |  |
| 134 | `PAYELEMENTIT104AMT` | DECIMAL(11,4) |  |  |  |  |
| 135 | `PAYELEMENTWFC300DESP` | VARCHAR(200) |  |  |  |  |
| 136 | `PAYELEMENTWFC300AMT` | DECIMAL(11,4) |  |  |  |  |
| 137 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 138 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKSALARYWAGEDEDUCTIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.EMPLOYEECODE,
       t.PAYELEMENTSLN300DESP,
       t.PAYELEMENTSLN300AMT,
       t.PAYELEMENTHLN300DESP,
       t.PAYELEMENTHLN301DESP,
       t.PAYELEMENTHLN300AMT,
       t.PAYELEMENTHLN301AMT,
       t.PAYELEMENTBGD300DESP,
       t.PAYELEMENTBGD300AMT,
       t.PAYELEMENTSHL300DESP
FROM   DB2ADMIN.WRKSALARYWAGEDEDUCTION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
