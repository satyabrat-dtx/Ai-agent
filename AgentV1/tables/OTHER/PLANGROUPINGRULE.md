# DB2ADMIN.PLANGROUPINGRULE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 4
- **Primary key**: `COMPANYCODE`, `RESERVEDITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 2 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 31200

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `RESERVEDITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `RULE` | INTEGER | NOT NULL |  |  |  |
| 3 | `RESERVEDITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |

## References (this table → parent) — 2

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PLANGROUPINGRULE.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_RESERVEDITEMTYPE` | `RESERVEDITEMTYPECOMPANYCODE`, `RESERVEDITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PLANGROUPINGRULE.RESERVEDITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PLANGROUPINGRULE.RESERVEDITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.RESERVEDITEMTYPECODE,
       t.RULE,
       t.RESERVEDITEMTYPECOMPANYCODE
FROM   DB2ADMIN.PLANGROUPINGRULE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
