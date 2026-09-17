# DB2ADMIN.WRKHIREDECISION

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `CREATIONTIMESTAMP`, `CREATIONUSER`, `COMPANYCODE`, `LINE`, `APPLICANTID`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 170852

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `CHOOSE` | SMALLINT | NOT NULL |  |  |  |
| 2 | `CREATIONUSER` | CHAR(50) | NOT NULL | PK | primary_key audit | User who created the row (audit). |
| 3 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 4 | `APPLICANTID` | BIGINT | NOT NULL | PK | primary_key |  |
| 5 | `APPLICANTNAME` | CHAR(100) |  |  |  |  |
| 6 | `SCORE` | CHAR(100) |  |  |  |  |
| 7 | `RATING` | CHAR(100) |  |  |  |  |
| 8 | `STATUS` | INTEGER | NOT NULL |  |  |  |
| 9 | `REASON` | CHAR(100) |  |  |  |  |
| 10 | `APPROVEDBYCODE` | CHAR(9) |  |  |  |  |
| 11 | `APPROVEDDATE` | DATE |  |  |  |  |
| 12 | `DIVISIONCODE` | CHAR(3) |  |  |  | Division within a company; second-level organisational discriminator. |
| 13 | `FACTORYCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 14 | `FACTORYCODE` | CHAR(8) |  |  |  |  |
| 15 | `DEPARTMENTDEPARTMENTCODE` | CHAR(8) |  |  |  |  |
| 16 | `SECTIONSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 17 | `SECTIONSECTIONCODE` | CHAR(6) |  |  |  |  |
| 18 | `MATESSECTIONICSTABLECODE` | CHAR(4) |  |  |  |  |
| 19 | `MATYPEMACHINETYPEICSTABLECODE` | CHAR(4) |  |  |  |  |
| 20 | `MACHINETYPEMACHINETYPECODE` | CHAR(6) |  |  |  |  |
| 21 | `OFFERDATE` | DATE |  |  |  |  |
| 22 | `JOININGDATE` | DATE |  |  |  |  |
| 23 | `LINE` | BIGINT | NOT NULL | PK | primary_key |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKHIREDECISIONUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.CHOOSE,
       t.CREATIONUSER,
       t.COMPANYCODE,
       t.APPLICANTID,
       t.APPLICANTNAME,
       t.SCORE,
       t.RATING,
       t.STATUS,
       t.REASON,
       t.APPROVEDBYCODE,
       t.APPROVEDDATE
FROM   DB2ADMIN.WRKHIREDECISION t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
