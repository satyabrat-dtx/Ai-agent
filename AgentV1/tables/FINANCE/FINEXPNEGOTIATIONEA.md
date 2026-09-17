# DB2ADMIN.FINEXPNEGOTIATIONEA

- **Module**: `FINANCE` (high confidence — table name starts with 'FIN')
- **Roles**: `business_data`
- **Columns**: 11
- **Primary key**: `COMPANYCODE`, `NEGOTIATIONCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 176717

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `NEGOTIATIONCODE` | CHAR(5) | NOT NULL | PK | primary_key |  |
| 2 | `CODE` | CHAR(5) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `BANKGLCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 4 | `BANKGLCODE` | CHAR(20) |  | FK | foreign_key |  |
| 5 | `BANKREFNO` | CHAR(20) |  |  |  |  |
| 6 | `BANKREFDATE` | DATE |  |  |  |  |
| 7 | `ADVANCEAMOUNTUSD` | DECIMAL(18,5) |  |  |  |  |
| 8 | `AVERAGERATE` | DECIMAL(18,5) |  |  |  |  |
| 9 | `CURRENTADJUSTMENT` | DECIMAL(18,5) |  |  |  |  |
| 10 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `GLMASTER_BANKGL` | `BANKGLCOMPANYCODE`, `BANKGLCODE` | [`GLMASTER`](../CORE_MASTER/GLMASTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `FINEXPNEGOTIATIONEA.BANKGLCOMPANYCODE = GLMASTER.COMPANYCODE AND FINEXPNEGOTIATIONEA.BANKGLCODE = GLMASTER.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `FINEXPNEGOTIATIONEAUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.NEGOTIATIONCODE,
       t.CODE,
       t.BANKGLCOMPANYCODE,
       t.BANKGLCODE,
       t.BANKREFNO,
       t.BANKREFDATE,
       t.ADVANCEAMOUNTUSD,
       t.AVERAGERATE,
       t.CURRENTADJUSTMENT,
       t.ABSUNIQUEID
FROM   DB2ADMIN.FINEXPNEGOTIATIONEA t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
