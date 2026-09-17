# DB2ADMIN.WRKQAOK

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `DIVISIONCODE`, `DEPARTMENTCODE`, `LABLOCUSERGENERICGROUPTYPECODE`, `LABLOCCODE`, `FROMDATE`, `TODATE`, `SAMPLEREFSHIFT`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 85848

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `DIVISIONCODE` | CHAR(3) | NOT NULL | PK | primary_key | Division within a company; second-level organisational discriminator. |
| 3 | `DEPARTMENTCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 4 | `LABLOCUSERGENGRPTYPECMYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 5 | `LABLOCUSERGENERICGROUPTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 6 | `LABLOCCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `FROMDATE` | DATE | NOT NULL | PK | primary_key | Inclusive start of a validity period. |
| 8 | `TODATE` | DATE | NOT NULL | PK | primary_key | End of a validity period. |
| 9 | `SAMPLEREFSHIFT` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 10 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 11 | `BEAMNO` | CHAR(50) |  |  |  |  |
| 12 | `SONO` | CHAR(15) |  |  |  |  |
| 13 | `IBNO` | CHAR(15) |  |  |  |  |
| 14 | `CUSTOMER` | CHAR(10) |  |  |  |  |
| 15 | `SHADE` | CHAR(10) |  |  |  |  |
| 16 | `MTRS` | DECIMAL(15,5) |  |  |  |  |
| 17 | `REMARK` | CHAR(50) |  |  |  |  |
| 18 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKQAOKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.DIVISIONCODE,
       t.DEPARTMENTCODE,
       t.LABLOCUSERGENGRPTYPECMYCODE,
       t.LABLOCUSERGENERICGROUPTYPECODE,
       t.LABLOCCODE,
       t.FROMDATE,
       t.TODATE,
       t.SAMPLEREFSHIFT,
       t.LINENO,
       t.BEAMNO
FROM   DB2ADMIN.WRKQAOK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
