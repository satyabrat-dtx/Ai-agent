# DB2ADMIN.WRKFINOUTSTANDINGCHECK

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 10
- **Primary key**: `CREATIONTIMESTAMP`, `COMPANYCODE`, `FINANCIALYEARCODE`, `BUSINESSUNITCODE`, `GLCODE`, `SLCUSTOMERSUPPLIERTYPE`, `SLCUSTOMERSUPPLIERCODE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 181391

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 2 | `FINANCIALYEARCODE` | DECIMAL(4,0) | NOT NULL | PK | primary_key |  |
| 3 | `BUSINESSUNITCODE` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 4 | `GLCODE` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 5 | `SLCUSTOMERSUPPLIERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 6 | `SLCUSTOMERSUPPLIERCODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 7 | `DOCUMENTLINEBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 8 | `OPNDOCUMENTBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINOUTSTANDINGCHECKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.COMPANYCODE,
       t.FINANCIALYEARCODE,
       t.BUSINESSUNITCODE,
       t.GLCODE,
       t.SLCUSTOMERSUPPLIERTYPE,
       t.SLCUSTOMERSUPPLIERCODE,
       t.DOCUMENTLINEBALANCE,
       t.OPNDOCUMENTBALANCE,
       t.ABSUNIQUEID
FROM   DB2ADMIN.WRKFINOUTSTANDINGCHECK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
