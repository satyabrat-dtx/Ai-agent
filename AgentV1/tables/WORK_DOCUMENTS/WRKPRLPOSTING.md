# DB2ADMIN.WRKPRLPOSTING

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 40
- **Primary key**: `COMPANYCODE`, `ATTENDANCETYPECODE`, `PAYROLLCODE`, `PROCESSPERIOD`, `DIVISIONCODE`, `FACTORYCODE`, `CATEGORYCODE`, `SUBCATEGORYCODE`, `COSTCENTERCODE`, `PAYELEMENTTYPE`, `PAYELEMENTCODE`, `LOANADVANCEFLAG`, `EMPLOYEECODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 169713

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ATTENDANCETYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `PAYROLLCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `PROCESSPERIOD` | INTEGER | NOT NULL | PK | primary_key |  |
| 4 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 5 | `FACTORYCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `CATEGORYCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 7 | `SUBCATEGORYCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 8 | `COSTCENTERCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 9 | `PAYELEMENTTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 10 | `PAYELEMENTCODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 11 | `LOANADVANCEFLAG` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 12 | `EMPLOYEECODE` | CHAR(9) | NOT NULL | PK | primary_key |  |
| 13 | `EMPLOYEEWISE` | CHAR(2) | NOT NULL |  |  |  |
| 14 | `DEBITGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 15 | `CREDITGLCODE` | CHAR(20) | NOT NULL |  |  |  |
| 16 | `AMTCALCULATED` | DECIMAL(11,4) | NOT NULL |  |  |  |
| 17 | `GLMAPPINGABSUNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 18 | `FIRSTUSERGRPUSERGENGRPTECMYCOD` | CHAR(3) |  |  |  |  |
| 19 | `FIRSTUSERGRPUSERGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 20 | `FIRSTUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 21 | `SNDUSERGRPUSERGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 22 | `SNDUSERGRPUSERGENGRPTYPECODE` | CHAR(3) |  |  |  |  |
| 23 | `SECONDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 24 | `THIRDUSERGRPUSERGENGRPTECMYCOD` | CHAR(3) |  |  |  |  |
| 25 | `THIRDUSERGRPUSERGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 26 | `THIRDUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 27 | `FRUSERGRPUSERGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 28 | `FRUSERGRPUSERGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 29 | `FOURTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 30 | `FIFTHUSERGRPUSERGENGRPTECMYCOD` | CHAR(3) |  |  |  |  |
| 31 | `FIFTHUSERGRPUSERGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 32 | `FIFTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 33 | `SIXTHUSERGRPUSERGENGRPTECMYCOD` | CHAR(3) |  |  |  |  |
| 34 | `SIXTHUSERGRPUSERGENGRPTECODE` | CHAR(3) |  |  |  |  |
| 35 | `SIXTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 36 | `SEUSERGRPUSERGENGRPTECMYCODE` | CHAR(3) |  |  |  |  |
| 37 | `SEUSERGRPUSERGENGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 38 | `SEVENTHUSERGRPCODE` | CHAR(10) |  |  |  |  |
| 39 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPRLPOSTINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ATTENDANCETYPECODE,
       t.PAYROLLCODE,
       t.PROCESSPERIOD,
       t.DIVISIONCODE,
       t.FACTORYCODE,
       t.CATEGORYCODE,
       t.SUBCATEGORYCODE,
       t.COSTCENTERCODE,
       t.PAYELEMENTTYPE,
       t.PAYELEMENTCODE,
       t.LOANADVANCEFLAG
FROM   DB2ADMIN.WRKPRLPOSTING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
