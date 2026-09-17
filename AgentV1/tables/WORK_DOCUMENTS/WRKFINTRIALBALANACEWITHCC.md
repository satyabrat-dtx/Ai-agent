# DB2ADMIN.WRKFINTRIALBALANACEWITHCC

- **Module**: `WORK_DOCUMENTS` (medium confidence — table name starts with 'WRK')
- **Roles**: `business_data`
- **Columns**: 13
- **Primary key**: `CREATIONTIMESTAMP`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 227316

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `CREATIONTIMESTAMP` | BIGINT | NOT NULL | PK | primary_key audit |  |
| 1 | `LINENO` | INTEGER | NOT NULL | PK | primary_key |  |
| 2 | `COMPANYCODE` | CHAR(3) |  |  | tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `FINANCIALYEARCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 4 | `FINANCIALYEARCODE` | DECIMAL(4,0) |  |  |  |  |
| 5 | `BUSINESSUNITCODE` | CHAR(10) |  |  |  |  |
| 6 | `GLCOMPANYCODE` | CHAR(3) |  |  |  |  |
| 7 | `GLCODE` | CHAR(20) |  |  |  |  |
| 8 | `GLDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 9 | `COSTCENTERCODE` | CHAR(20) |  |  |  |  |
| 10 | `FINOPENINGBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 11 | `TRANSACTIONBALANCE` | DECIMAL(18,5) |  |  |  |  |
| 12 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WRKFINTRIALBALANACEWITHCCUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.CREATIONTIMESTAMP,
       t.LINENO,
       t.COMPANYCODE,
       t.FINANCIALYEARCOMPANYCODE,
       t.FINANCIALYEARCODE,
       t.BUSINESSUNITCODE,
       t.GLCOMPANYCODE,
       t.GLCODE,
       t.GLDESCRIPTION,
       t.COSTCENTERCODE,
       t.FINOPENINGBALANCE,
       t.TRANSACTIONBALANCE
FROM   DB2ADMIN.WRKFINTRIALBALANACEWITHCC t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
