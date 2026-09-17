# DB2ADMIN.ORDERBOX

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 14
- **Primary key**: `COMPANYCODE`, `ORDERTYPE`, `ORDERCOUNTERCODE`, `ORDERCODE`, `ITEMTYPECODE`, `CONTAINERSUBCODE01`
- **FK degree**: referenced by 0 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 58830

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ORDERTYPE` | CHAR(1) | NOT NULL | PK | primary_key |  |
| 2 | `ORDERCOUNTERCODE` | CHAR(8) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `ORDERCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `PREVIOUSQUANTITY` | INTEGER | NOT NULL |  |  |  |
| 7 | `QUANTITY` | INTEGER | NOT NULL |  |  |  |
| 8 | `USEDQUANTITY` | INTEGER | NOT NULL |  |  |  |
| 9 | `ADDITIONALNOTES` | LONG VARCHAR |  |  |  |  |
| 10 | `ORDERCOUNTERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 11 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 12 | `CONTAINERCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 13 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ORDERBOX.COMPANYCODE = COMPANY.CODE` |
| `CONTAINER_CONTAINER` | `CONTAINERCOMPANYCODE`, `ITEMTYPECODE`, `CONTAINERSUBCODE01` | [`CONTAINER`](../CORE_MASTER/CONTAINER.md) | `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01` | RESTRICT | `ORDERBOX.CONTAINERCOMPANYCODE = CONTAINER.COMPANYCODE AND ORDERBOX.ITEMTYPECODE = CONTAINER.ITEMTYPECODE AND ORDERBOX.CONTAINERSUBCODE01 = CONTAINER.SUBCODE01` |
| `COUNTER_ORDERCOUNTER` | `ORDERCOUNTERCOMPANYCODE`, `ORDERCOUNTERCODE` | [`COUNTER`](../CORE_MASTER/COUNTER.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERBOX.ORDERCOUNTERCOMPANYCODE = COUNTER.COMPANYCODE AND ORDERBOX.ORDERCOUNTERCODE = COUNTER.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ORDERBOX.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ORDERBOX.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `ORDERBOXUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ORDERTYPE,
       t.ORDERCOUNTERCODE,
       t.ORDERCODE,
       t.ITEMTYPECODE,
       t.CONTAINERSUBCODE01,
       t.PREVIOUSQUANTITY,
       t.QUANTITY,
       t.USEDQUANTITY,
       t.ADDITIONALNOTES,
       t.ORDERCOUNTERCOMPANYCODE,
       t.ITEMTYPECOMPANYCODE
FROM   DB2ADMIN.ORDERBOX t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
