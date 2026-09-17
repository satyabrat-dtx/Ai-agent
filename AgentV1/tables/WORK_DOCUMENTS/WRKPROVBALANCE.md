# DB2ADMIN.WRKPROVBALANCE

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 18
- **Primary key**: `COMPANYCODE`, `CREATIONTIMESTAMP`, `LINENO`, `ASONDATE`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 178794

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 2 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `BSLINETEMCODE` | CHAR(10) |  |  |  |  |
| 4 | `CALFLAG` | INTEGER | NOT NULL |  |  |  |
| 5 | `SEQUENCENO` | DECIMAL(6,0) |  |  |  |  |
| 6 | `ISHEADING` | SMALLINT | NOT NULL |  |  |  |
| 7 | `ASONDATE` | DATE | NOT NULL | PK | primary_key |  |
| 8 | `GLCODE` | CHAR(20) |  |  |  |  |
| 9 | `BSTEMPLATECODE` | CHAR(10) |  |  |  |  |
| 10 | `PROCREDITAMT` | DECIMAL(18,5) |  |  |  |  |
| 11 | `PRODEBITAMT` | DECIMAL(18,5) |  |  |  |  |
| 12 | `TOTPROVAMT` | DECIMAL(18,5) |  |  |  |  |
| 13 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 14 | `PROVGLAMT` | DECIMAL(18,5) |  |  |  |  |
| 15 | `YEARFLAG` | SMALLINT | NOT NULL |  |  |  |
| 16 | `DETAILFLAG` | SMALLINT | NOT NULL |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKPROVBALANCEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.CREATIONTIMESTAMP,
       t.LINENO,
       t.BSLINETEMCODE,
       t.CALFLAG,
       t.SEQUENCENO,
       t.ISHEADING,
       t.ASONDATE,
       t.GLCODE,
       t.BSTEMPLATECODE,
       t.PROCREDITAMT,
       t.PRODEBITAMT
FROM   DB2ADMIN.WRKPROVBALANCE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
