# DB2ADMIN.LUTENTRY

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 9
- **Primary key**: `COMPANYCODE`, `SCHEMETYPECODE`, `LUTNO`
- **FK degree**: referenced by 1 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140112

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `SCHEMETYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `LUTNO` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 3 | `LUTDATE` | DATE | NOT NULL |  |  |  |
| 4 | `LUTAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 5 | `LUTUTILISEDAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 6 | `LUTBALANCEAMOUNT` | DECIMAL(18,5) | NOT NULL |  |  |  |
| 7 | `LUTVALIDITY` | DATE |  |  |  |  |
| 8 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `LUTENTRY.COMPANYCODE = COMPANY.CODE` |
| `SCHEMETYPE_SCHEMETYPE` | `COMPANYCODE`, `SCHEMETYPECODE` | [`SCHEMETYPE`](../OTHER/SCHEMETYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `LUTENTRY.COMPANYCODE = SCHEMETYPE.COMPANYCODE AND LUTENTRY.SCHEMETYPECODE = SCHEMETYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `LUTENTRY_LINE` | [`LUTENTRYLINE`](../OTHER/LUTENTRYLINE.md) | `LUTENTRYCOMPANYCODE`, `LUTENTRYSCHEMETYPECODE`, `LUTENTRYLUTNO` | `LUTENTRYLINE.LUTENTRYCOMPANYCODE = LUTENTRY.COMPANYCODE AND LUTENTRYLINE.LUTENTRYSCHEMETYPECODE = LUTENTRY.SCHEMETYPECODE AND LUTENTRYLINE.LUTENTRYLUTNO = LUTENTRY.LUTNO` |

## Indexes

- `LUTENTRYUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.SCHEMETYPECODE,
       t.LUTNO,
       t.LUTDATE,
       t.LUTAMOUNT,
       t.LUTUTILISEDAMOUNT,
       t.LUTBALANCEAMOUNT,
       t.LUTVALIDITY,
       t.ABSUNIQUEID
FROM   DB2ADMIN.LUTENTRY t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
