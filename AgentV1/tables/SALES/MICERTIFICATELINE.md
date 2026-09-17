# DB2ADMIN.MICERTIFICATELINE

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 16
- **Primary key**: `MICERTIFICATECOMPANYCODE`, `MICERTIFICATEDIVISIONCODE`, `MICERTIFICATEMICNO`, `LINENO`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 140279

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `MICERTIFICATECOMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 1 | `MICERTIFICATEDIVISIONCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `MICERTIFICATEMICNO` | CHAR(12) | NOT NULL | PK FK | primary_key foreign_key |  |
| 3 | `LINENO` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 4 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 5 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 6 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 7 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 8 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 9 | `PRIMARYQTY` | DECIMAL(15,5) | NOT NULL |  |  |  |
| 10 | `PRIMARYUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 11 | `SECONDARYQTY` | DECIMAL(15,5) |  |  |  |  |
| 12 | `SECONDARYUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 13 | `PACKINGQTY` | DECIMAL(15,5) |  |  |  |  |
| 14 | `PACKINGUMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 15 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `MICERTIFICATELINE.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND MICERTIFICATELINE.ITEMTYPECODE = ITEMTYPE.CODE` |
| `MICERTIFICATE_LINE` | `MICERTIFICATECOMPANYCODE`, `MICERTIFICATEDIVISIONCODE`, `MICERTIFICATEMICNO` | [`MICERTIFICATE`](../SALES/MICERTIFICATE.md) | `COMPANYCODE`, `DIVISIONCODE`, `MICNO` | RESTRICT | `MICERTIFICATELINE.MICERTIFICATECOMPANYCODE = MICERTIFICATE.COMPANYCODE AND MICERTIFICATELINE.MICERTIFICATEDIVISIONCODE = MICERTIFICATE.DIVISIONCODE AND MICERTIFICATELINE.MICERTIFICATEMICNO = MICERTIFICATE.MICNO` |
| `UNITOFMEASURE_PACKINGUM` | `PACKINGUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `MICERTIFICATELINE.PACKINGUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_PRIMARYUM` | `PRIMARYUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `MICERTIFICATELINE.PRIMARYUMCODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_SECONDARYUM` | `SECONDARYUMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `MICERTIFICATELINE.SECONDARYUMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `MICERTIFICATELINEUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.MICERTIFICATECOMPANYCODE,
       t.MICERTIFICATEDIVISIONCODE,
       t.MICERTIFICATEMICNO,
       t.LINENO,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.PRIMARYQTY,
       t.PRIMARYUMCODE,
       t.SECONDARYQTY
FROM   DB2ADMIN.MICERTIFICATELINE t
FETCH FIRST 100 ROWS ONLY;
```
