# DB2ADMIN.CHARGETRANSACTIONLINK

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `TRANSACTIONNUMBER`, `ACCOUNTTRANSACTIONNUMBER`, `CHARGESITEMTYPECODE`, `CHARGESSUBCODE01`
- **FK degree**: referenced by 0 constraint(s), references 0 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 94679

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 2 | `ACCOUNTTRANSACTIONNUMBER` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 3 | `CHARGESCOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 4 | `CHARGESITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `CHARGESSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 6 | `VALUEINSYSTEMCURRENCY` | DECIMAL(18,5) |  |  |  |  |
| 7 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 8 | `VALUEINSECONDCURRENCY` | DECIMAL(18,5) |  |  |  |  |

## References (this table → parent) — 0

_None._

## Referenced by (child → this table) — 0

_None._

## Indexes

- `CHARGETRANSACTIONLINKUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TRANSACTIONNUMBER,
       t.ACCOUNTTRANSACTIONNUMBER,
       t.CHARGESCOMPANYCODE,
       t.CHARGESITEMTYPECODE,
       t.CHARGESSUBCODE01,
       t.VALUEINSYSTEMCURRENCY,
       t.ABSUNIQUEID,
       t.VALUEINSECONDCURRENCY
FROM   DB2ADMIN.CHARGETRANSACTIONLINK t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
