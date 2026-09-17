# DB2ADMIN.WRKQASTATUSREPORT

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 45
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `DIVISIONCODE`, `DEPARTMENTCODE`, `ITEMTYPECODE`, `QATEMPLATECODE`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85768

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `DIVISIONCODE` | CHAR(8) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `DEPARTMENTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `QATEMPLATECODE` | CHAR(6) | NOT NULL | PK | primary_key |  |
| 6 | `REQUESTNO` | CHAR(25) |  |  |  |  |
| 7 | `ENTRYDATE` | DATE |  |  |  |  |
| 8 | `ACTUALENTRYDATE` | DATE |  |  |  |  |
| 9 | `CUSTOMERTYPE` | CHAR(8) |  |  |  |  |
| 10 | `CUSTOMERCODE` | CHAR(8) |  |  |  |  |
| 11 | `SUBCODE1` | CHAR(20) |  |  |  |  |
| 12 | `SUBCODE2` | CHAR(10) |  |  |  |  |
| 13 | `SUBCODE3` | CHAR(10) |  |  |  |  |
| 14 | `SUBCODE4` | CHAR(10) |  |  |  |  |
| 15 | `SUBCODE5` | CHAR(10) |  |  |  |  |
| 16 | `SUBCODE6` | CHAR(10) |  |  |  |  |
| 17 | `SUBCODE7` | CHAR(10) |  |  |  |  |
| 18 | `SUBCODE8` | CHAR(10) |  |  |  |  |
| 19 | `SUBCODE9` | CHAR(10) |  |  |  |  |
| 20 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 21 | `PRODDESCRIPTION` | VARCHAR(100) |  |  |  |  |
| 22 | `REQUESTSTATUS` | INTEGER | NOT NULL |  |  |  |
| 23 | `LABLOCATIONCODE` | CHAR(10) |  |  |  |  |
| 24 | `WHLOTNO` | CHAR(10) |  |  |  |  |
| 25 | `MRNNO` | INTEGER | NOT NULL |  |  |  |
| 26 | `REMARKS` | CHAR(50) |  |  |  |  |
| 27 | `LABCOMMENT` | VARCHAR(200) |  |  |  |  |
| 28 | `SAMPLEREFNO` | CHAR(20) |  |  |  |  |
| 29 | `TESTTYPE` | CHAR(10) |  |  |  |  |
| 30 | `DEPARTCMT` | VARCHAR(200) |  |  |  |  |
| 31 | `SAMPLETYPE` | INTEGER | NOT NULL |  |  |  |
| 32 | `TESTCODE` | CHAR(6) |  |  |  |  |
| 33 | `TESTDESP` | VARCHAR(100) |  |  |  |  |
| 34 | `STDVALUE` | CHAR(25) |  |  |  |  |
| 35 | `STUMCODE` | CHAR(3) |  |  |  |  |
| 36 | `STDMINIMUM` | CHAR(25) |  |  |  |  |
| 37 | `STDMINUMCODE` | CHAR(3) |  |  |  |  |
| 38 | `STDMAXIMUM` | CHAR(25) |  |  |  |  |
| 39 | `STDMAXUMCODE` | CHAR(3) |  |  |  |  |
| 40 | `STDACTVALUE` | CHAR(25) |  |  |  |  |
| 41 | `STDACTUMCODE` | CHAR(3) |  |  |  |  |
| 42 | `QUALITYGROUPCODE` | CHAR(10) |  |  |  |  |
| 43 | `LINENO` | BIGINT | NOT NULL | PK | primary_key |  |
| 44 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKQASTATUSREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.DIVISIONCODE,
       t.DEPARTMENTCODE,
       t.ITEMTYPECODE,
       t.QATEMPLATECODE,
       t.REQUESTNO,
       t.ENTRYDATE,
       t.ACTUALENTRYDATE,
       t.CUSTOMERTYPE,
       t.CUSTOMERCODE,
       t.SUBCODE1
FROM   DB2ADMIN.WRKQASTATUSREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
