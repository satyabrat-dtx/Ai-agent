# DB2ADMIN.ROUTINGITEMSUBCODEFORREPORT

- **Module**: `PRODUCTION` (high confidence — table name starts with 'ROUTING')
- **Roles**: `business_data`
- **Columns**: 44
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 28626

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `ITEMTYPEDESCRIPTION` | VARCHAR(80) |  |  |  |  |
| 3 | `LASTPRIMARYSUBCODE` | INTEGER | NOT NULL |  |  |  |
| 4 | `LASTSUBCODE` | INTEGER | NOT NULL |  |  |  |
| 5 | `SHORTDESCRIPTION01` | VARCHAR(80) |  |  |  |  |
| 6 | `DATATYPE01` | CHAR(2) |  |  |  |  |
| 7 | `OUTPUTSEPARATOR01` | CHAR(2) |  |  |  |  |
| 8 | `SHORTDESCRIPTION02` | VARCHAR(80) |  |  |  |  |
| 9 | `DATATYPE02` | CHAR(2) |  |  |  |  |
| 10 | `OUTPUTSEPARATOR02` | CHAR(2) |  |  |  |  |
| 11 | `SHORTDESCRIPTION03` | VARCHAR(80) |  |  |  |  |
| 12 | `DATATYPE03` | CHAR(2) |  |  |  |  |
| 13 | `OUTPUTSEPARATOR03` | CHAR(2) |  |  |  |  |
| 14 | `SHORTDESCRIPTION04` | VARCHAR(80) |  |  |  |  |
| 15 | `DATATYPE04` | CHAR(2) |  |  |  |  |
| 16 | `OUTPUTSEPARATOR04` | CHAR(2) |  |  |  |  |
| 17 | `SHORTDESCRIPTION05` | VARCHAR(80) |  |  |  |  |
| 18 | `DATATYPE05` | CHAR(2) |  |  |  |  |
| 19 | `OUTPUTSEPARATOR05` | CHAR(2) |  |  |  |  |
| 20 | `SHORTDESCRIPTION06` | VARCHAR(80) |  |  |  |  |
| 21 | `DATATYPE06` | CHAR(2) |  |  |  |  |
| 22 | `OUTPUTSEPARATOR06` | CHAR(2) |  |  |  |  |
| 23 | `SHORTDESCRIPTION07` | VARCHAR(80) |  |  |  |  |
| 24 | `DATATYPE07` | CHAR(2) |  |  |  |  |
| 25 | `OUTPUTSEPARATOR07` | CHAR(2) |  |  |  |  |
| 26 | `SHORTDESCRIPTION08` | VARCHAR(80) |  |  |  |  |
| 27 | `DATATYPE08` | CHAR(2) |  |  |  |  |
| 28 | `OUTPUTSEPARATOR08` | CHAR(2) |  |  |  |  |
| 29 | `SHORTDESCRIPTION09` | VARCHAR(80) |  |  |  |  |
| 30 | `DATATYPE09` | CHAR(2) |  |  |  |  |
| 31 | `OUTPUTSEPARATOR09` | CHAR(2) |  |  |  |  |
| 32 | `SHORTDESCRIPTION10` | VARCHAR(80) |  |  |  |  |
| 33 | `DATATYPE10` | CHAR(2) |  |  |  |  |
| 34 | `OUTPUTSEPARATOR10` | CHAR(2) |  |  |  |  |
| 35 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 36 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 37 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 38 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 39 | `OWNINGCOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 40 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 41 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 42 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 43 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ROUTINGITEMSUBCODEFORREPORT.COMPANYCODE = COMPANY.CODE` |
| `COMPANY_OWNINGCOMPANY` | `OWNINGCOMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `ROUTINGITEMSUBCODEFORREPORT.OWNINGCOMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `ROUTINGITEMSUBCODEFORREPORT.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND ROUTINGITEMSUBCODEFORREPORT.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `RTGITEMSUBCODEFORREPORTUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECODE,
       t.ITEMTYPEDESCRIPTION,
       t.LASTPRIMARYSUBCODE,
       t.LASTSUBCODE,
       t.SHORTDESCRIPTION01,
       t.DATATYPE01,
       t.OUTPUTSEPARATOR01,
       t.SHORTDESCRIPTION02,
       t.DATATYPE02,
       t.OUTPUTSEPARATOR02,
       t.SHORTDESCRIPTION03
FROM   DB2ADMIN.ROUTINGITEMSUBCODEFORREPORT t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
