# DB2ADMIN.SERVICETRNSERVICETRNLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 8
- **Primary key**: `COMPANYCODE`, `TRANSACTIONNUMBER`, `TRANSACTIONDETAILNUMBER`, `SERVICETRANSACTIONNUMBER`, `SERVICETRANSACTIONDETAILNUMBER`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 111674

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `TRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 3 | `SERVICETRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `SERVICETRANSACTIONDETAILNUMBER` | INTEGER | NOT NULL | PK | primary_key |  |
| 5 | `VALUEINSYSTEMCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 6 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 7 | `VALUEINSECONDCURRENCY` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SERVICETRNSERVICETRNLINK.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SERVICETRNSERVICETRNLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.TRANSACTIONDETAILNUMBER,
       t.SERVICETRANSACTIONNUMBER,
       t.SERVICETRANSACTIONDETAILNUMBER,
       t.VALUEINSYSTEMCURRENCY,
       t.ABSUNIQUEID,
       t.VALUEINSECONDCURRENCY
FROM   DB2ADMIN.SERVICETRNSERVICETRNLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
