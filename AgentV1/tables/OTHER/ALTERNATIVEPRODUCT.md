# DB2ADMIN.ALTERNATIVEPRODUCT

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `ITEMTYPEAFICODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 1 constraint(s), references 4 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 72489

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DIVISIONCODE` | CHAR(3) |  | FK | foreign_key | Division within a company; second-level organisational discriminator. |
| 2 | `ALLOWEDDIVISIONS` | CHAR(90) |  |  |  |  |
| 3 | `VALIDITYSTATUS` | CHAR(2) | NOT NULL |  |  |  |
| 4 | `ORIGINALITEMFULLREQUIRED` | SMALLINT | NOT NULL |  |  |  |
| 5 | `ITEMTYPEAFICODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 6 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 15 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 16 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `ITEMTYPEAFICOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 23 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 24 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 4

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ALTERNATIVEPRODUCT.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ALTERNATIVEPRODUCT.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `DIVISION_DIVISION` | `COMPANYCODE`, `DIVISIONCODE` | [`DIVISION`](../CORE_MASTER/DIVISION.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ALTERNATIVEPRODUCT.COMPANYCODE = DIVISION.COMPANYCODE AND ALTERNATIVEPRODUCT.DIVISIONCODE = DIVISION.CODE` |
| `ITEMTYPE_ITEMTYPEAFI` | `ITEMTYPEAFICOMPANYCODE`, `ITEMTYPEAFICODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ALTERNATIVEPRODUCT.ITEMTYPEAFICOMPANYCODE = ITEMTYPE.COMPANYCODE AND ALTERNATIVEPRODUCT.ITEMTYPEAFICODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `ALTERNATIVEPRODUCT_SUBSTITUTEPRODUCT` | [`SUBSTITUTEPRODUCT`](../OTHER/SUBSTITUTEPRODUCT.md) | `ALTERNATIVEPRODUCTCOMPANYCODE`, `ALTPRODUCTITEMTYPEAFICODE`, `ALTERNATIVEPRODUCTSUBCODE01`, `ALTERNATIVEPRODUCTSUBCODE02`, `ALTERNATIVEPRODUCTSUBCODE03`, `ALTERNATIVEPRODUCTSUBCODE04`, `ALTERNATIVEPRODUCTSUBCODE05`, `ALTERNATIVEPRODUCTSUBCODE06`, `ALTERNATIVEPRODUCTSUBCODE07`, `ALTERNATIVEPRODUCTSUBCODE08`, `ALTERNATIVEPRODUCTSUBCODE09`, `ALTERNATIVEPRODUCTSUBCODE10` | `SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTCOMPANYCODE = ALTERNATIVEPRODUCT.COMPANYCODE AND SUBSTITUTEPRODUCT.ALTPRODUCTITEMTYPEAFICODE = ALTERNATIVEPRODUCT.ITEMTYPEAFICODE AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE01 = ALTERNATIVEPRODUCT.SUBCODE01 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE02 = ALTERNATIVEPRODUCT.SUBCODE02 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE03 = ALTERNATIVEPRODUCT.SUBCODE03 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE04 = ALTERNATIVEPRODUCT.SUBCODE04 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE05 = ALTERNATIVEPRODUCT.SUBCODE05 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE06 = ALTERNATIVEPRODUCT.SUBCODE06 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE07 = ALTERNATIVEPRODUCT.SUBCODE07 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE08 = ALTERNATIVEPRODUCT.SUBCODE08 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE09 = ALTERNATIVEPRODUCT.SUBCODE09 AND SUBSTITUTEPRODUCT.ALTERNATIVEPRODUCTSUBCODE10 = ALTERNATIVEPRODUCT.SUBCODE10` |

## Indexes

- `ALTERNATIVEPRODUCTUID` (ABSUNIQUEID)
- `ALTPRODUCTS01` (COMPANYCODE, ITEMTYPEAFICODE, SUBCODE01, SUBCODE02, SUBCODE03, SUBCODE04, SUBCODE05, SUBCODE06, SUBCODE07, SUBCODE08, SUBCODE09, SUBCODE10, VALIDITYSTATUS)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DIVISIONCODE,
       t.ALLOWEDDIVISIONS,
       t.VALIDITYSTATUS,
       t.ORIGINALITEMFULLREQUIRED,
       t.ITEMTYPEAFICODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06
FROM   DB2ADMIN.ALTERNATIVEPRODUCT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
