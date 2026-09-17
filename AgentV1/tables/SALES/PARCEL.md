# DB2ADMIN.PARCEL

- **Module**: `SALES` (low confidence — FK neighbourhood: 1 of 1 related tables are SALES)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `PARCELCODE`
- **FK degree**: referenced by 1 constraint(s), references 6 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 26873

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `PARCELCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 2 | `PARCELTYPE` | CHAR(2) |  |  |  |  |
| 3 | `LONGDESCRIPTION` | VARCHAR(200) |  |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(80) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(120) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `VOLUME` | DECIMAL(15,5) |  |  |  |  |
| 7 | `VOLUMEUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `WIDTH` | DECIMAL(15,5) |  |  |  |  |
| 9 | `WIDTHUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 10 | `HEIGHT` | DECIMAL(15,5) |  |  |  |  |
| 11 | `HEIGHTUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 12 | `LENGTH` | DECIMAL(15,5) |  |  |  |  |
| 13 | `LENGTHUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `APPEARANCEDESCRIPTION` | VARCHAR(200) |  |  |  |  |
| 15 | `WEIGHTUNITOFMEASURECODE` | CHAR(3) |  | FK | foreign_key |  |
| 16 | `WEIGHTGROSS` | DECIMAL(15,5) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 22 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 23 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 6

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PARCEL.COMPANYCODE = COMPANY.CODE` |
| `UNITOFMEASURE_HEIGHTUNITOFMEASURE` | `HEIGHTUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PARCEL.HEIGHTUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_LENGTHUNITOFMEASURE` | `LENGTHUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PARCEL.LENGTHUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_VOLUMEUNITOFMEASURE` | `VOLUMEUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PARCEL.VOLUMEUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_WEIGHTUNITOFMEASURE` | `WEIGHTUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PARCEL.WEIGHTUNITOFMEASURECODE = UNITOFMEASURE.CODE` |
| `UNITOFMEASURE_WIDTHUNITOFMEASURE` | `WIDTHUNITOFMEASURECODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `PARCEL.WIDTHUNITOFMEASURECODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `PARCEL_PARCEL` | [`SALESPACKINGPARCEL`](../SALES/SALESPACKINGPARCEL.md) | `SALESPACKINGCOMPANYCODE`, `PARCELPARCELCODE` | `SALESPACKINGPARCEL.SALESPACKINGCOMPANYCODE = PARCEL.COMPANYCODE AND SALESPACKINGPARCEL.PARCELPARCELCODE = PARCEL.PARCELCODE` |

## Indexes

- `PARCELUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.PARCELCODE,
       t.PARCELTYPE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.VOLUME,
       t.VOLUMEUNITOFMEASURECODE,
       t.WIDTH,
       t.WIDTHUNITOFMEASURECODE,
       t.HEIGHT,
       t.HEIGHTUNITOFMEASURECODE
FROM   DB2ADMIN.PARCEL t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
