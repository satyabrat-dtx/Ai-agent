# DB2ADMIN.SERVICESIE

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 123648

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `TARIFFCODE` | CHAR(20) |  | FK | foreign_key |  |
| 6 | `TAXTEMPLATEDETAILTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 7 | `TAXTEMPLATEDETAILCODE` | CHAR(3) |  |  |  |  |
| 8 | `TAXTEMPLATEHEADERTEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 9 | `TAXTEMPLATEHEADERCODE` | CHAR(3) |  |  |  |  |
| 10 | `GSTWITHINSTATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 11 | `GSTWITHINSTATECODE` | CHAR(3) |  |  |  |  |
| 12 | `GSTINTERSTATETEMPLATETYPE` | CHAR(2) |  |  |  |  |
| 13 | `GSTINTERSTATECODE` | CHAR(3) |  |  |  |  |
| 14 | `INPUTCAPITAL` | INTEGER | NOT NULL |  |  |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `SERVICESIE.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `SERVICESIE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND SERVICESIE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `TARIFF_TARIFF` | `TARIFFCODE` | [`TARIFF`](../CORE_MASTER/TARIFF.md) | `CODE` | RESTRICT | `SERVICESIE.TARIFFCODE = TARIFF.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `SERVICESIEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.OWNINGCOMPANYCODE,
       t.TARIFFCODE,
       t.TAXTEMPLATEDETAILTEMPLATETYPE,
       t.TAXTEMPLATEDETAILCODE,
       t.TAXTEMPLATEHEADERTEMPLATETYPE,
       t.TAXTEMPLATEHEADERCODE,
       t.GSTWITHINSTATETEMPLATETYPE,
       t.GSTWITHINSTATECODE
FROM   DB2ADMIN.SERVICESIE t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
