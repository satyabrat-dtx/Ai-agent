# DB2ADMIN.EPCGAPPLICATIONEXPORTPRODUCT

- **Module**: `PURCHASING` (low confidence — FK neighbourhood: 1 of 1 related tables are PURCHASING)
- **Roles**: `business_data`
- **Columns**: 19
- **Primary key**: `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE`, `COMPANYCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 137952

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `EPCGAPPLICATIONCOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `EPCGAPPLICATIONCODE` | CHAR(30) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 3 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 4 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 5 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `SHIPMENTARTICLECODE` | CHAR(5) |  | FK | foreign_key |  |
| 16 | `ITEMDESCRIPTION` | CHAR(100) |  |  |  |  |
| 17 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 18 | `SHIPMENTARTICLECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `EPCGAPPLICATION_PRDEXPORTLINE` | `EPCGAPPLICATIONCOMPANYCODE`, `EPCGAPPLICATIONCODE` | [`EPCGAPPLICATION`](../PURCHASING/EPCGAPPLICATION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONEXPORTPRODUCT.EPCGAPPLICATIONCOMPANYCODE = EPCGAPPLICATION.COMPANYCODE AND EPCGAPPLICATIONEXPORTPRODUCT.EPCGAPPLICATIONCODE = EPCGAPPLICATION.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONEXPORTPRODUCT.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND EPCGAPPLICATIONEXPORTPRODUCT.ITEMTYPEAFICODE = ITEMTYPE.CODE` |
| `SHIPMENTARTICLE_SHIPMENTARTICLE` | `SHIPMENTARTICLECOMPANYCODE`, `SHIPMENTARTICLECODE` | [`SHIPMENTARTICLE`](../OTHER/SHIPMENTARTICLE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `EPCGAPPLICATIONEXPORTPRODUCT.SHIPMENTARTICLECOMPANYCODE = SHIPMENTARTICLE.COMPANYCODE AND EPCGAPPLICATIONEXPORTPRODUCT.SHIPMENTARTICLECODE = SHIPMENTARTICLE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `EPCGAPPEXPORTPRODUCTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.EPCGAPPLICATIONCOMPANYCODE,
       t.EPCGAPPLICATIONCODE,
       t.COMPANYCODE,
       t.ITEMTYPEAFICOMPANYCODE,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07
FROM   DB2ADMIN.EPCGAPPLICATIONEXPORTPRODUCT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
