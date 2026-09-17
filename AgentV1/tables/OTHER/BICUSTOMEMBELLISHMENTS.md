# DB2ADMIN.BICUSTOMEMBELLISHMENTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 60
- **Primary key**: `COMPANYCODE`, `CODE`
- **FK degree**: referenced by 0 constraint(s), references 5 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 34013

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `TYPECODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `CODE` | CHAR(10) | NOT NULL | PK | primary_key | Business (natural) key of a master-data table, typically the last primary-key column. |
| 3 | `LONGDESCRIPTION` | VARCHAR(100) | NOT NULL |  | description | Long human-readable label. |
| 4 | `SHORTDESCRIPTION` | VARCHAR(40) |  |  | description | Short human-readable label. |
| 5 | `SEARCHDESCRIPTION` | VARCHAR(60) |  |  | description | Normalised/uppercased label used for lookup and search screens. |
| 6 | `FRONTDISCHARGE` | SMALLINT | NOT NULL |  |  |  |
| 7 | `FRONTPLASTISOL` | SMALLINT | NOT NULL |  |  |  |
| 8 | `FRONTDISTRESS` | SMALLINT | NOT NULL |  |  |  |
| 9 | `FRONTFOILPAPER` | SMALLINT | NOT NULL |  |  |  |
| 10 | `FRONTFLOCKING` | SMALLINT | NOT NULL |  |  |  |
| 11 | `FRONTGRAPHICSTYLENOTES` | CLOB(1000000) |  |  |  |  |
| 12 | `FRONTCOLORVARIETY` | INTEGER | NOT NULL |  |  |  |
| 13 | `FRONTCOLORNOTES` | CLOB(1000000) |  |  |  |  |
| 14 | `FRONTGRAPHICSTYLENUMBER` | CHAR(10) |  |  |  |  |
| 15 | `FRONTEMBROIDERYCODE` | CHAR(10) |  | FK | foreign_key |  |
| 16 | `BACKDISCHARGE` | SMALLINT | NOT NULL |  |  |  |
| 17 | `BACKPLASTISOL` | SMALLINT | NOT NULL |  |  |  |
| 18 | `BACKDISTRESS` | SMALLINT | NOT NULL |  |  |  |
| 19 | `BACKFOILPAPER` | SMALLINT | NOT NULL |  |  |  |
| 20 | `BACKFLOCKING` | SMALLINT | NOT NULL |  |  |  |
| 21 | `BACKGRAPHICSTYLENOTES` | CLOB(1000000) |  |  |  |  |
| 22 | `BACKCOLORVARIETY` | INTEGER | NOT NULL |  |  |  |
| 23 | `BACKCOLORNOTES` | CLOB(1000000) |  |  |  |  |
| 24 | `BACKGRAPHICSTYLENUMBER` | CHAR(10) |  |  |  |  |
| 25 | `BACKEMBROIDERYCODE` | CHAR(10) |  | FK | foreign_key |  |
| 26 | `SLEEVEDISCHARGE` | SMALLINT | NOT NULL |  |  |  |
| 27 | `SLEEVEPLASTISOL` | SMALLINT | NOT NULL |  |  |  |
| 28 | `SLEEVEDISTRESS` | SMALLINT | NOT NULL |  |  |  |
| 29 | `SLEEVEFOILPAPER` | SMALLINT | NOT NULL |  |  |  |
| 30 | `SLEEVEFLOCKING` | SMALLINT | NOT NULL |  |  |  |
| 31 | `SLEEVEGRAPHICSTYLENOTES` | CLOB(1000000) |  |  |  |  |
| 32 | `SLEEVECOLORVARIETY` | INTEGER | NOT NULL |  |  |  |
| 33 | `SLEEVECOLORNOTES` | CLOB(1000000) |  |  |  |  |
| 34 | `SLEEVEGRAPHICSTYLENUMBER` | CHAR(10) |  |  |  |  |
| 35 | `SLEEVEEMBROIDERYCODE` | CHAR(10) |  | FK | foreign_key |  |
| 36 | `LAUNDRYCODE` | CHAR(10) |  | FK | foreign_key |  |
| 37 | `NOTES` | CLOB(1000000) |  |  |  |  |
| 38 | `PRICETICKET` | SMALLINT | NOT NULL |  |  |  |
| 39 | `SIZESTRIP` | SMALLINT | NOT NULL |  |  |  |
| 40 | `HANGTAG` | SMALLINT | NOT NULL |  |  |  |
| 41 | `HANGAR` | SMALLINT | NOT NULL |  |  |  |
| 42 | `POLYBAG` | SMALLINT | NOT NULL |  |  |  |
| 43 | `SPECIALBOXSIZE` | SMALLINT | NOT NULL |  |  |  |
| 44 | `USERFIELD01` | SMALLINT | NOT NULL |  |  |  |
| 45 | `USERFIELD02` | SMALLINT | NOT NULL |  |  |  |
| 46 | `USERFIELD03` | SMALLINT | NOT NULL |  |  |  |
| 47 | `USERFIELD04` | SMALLINT | NOT NULL |  |  |  |
| 48 | `USERFIELD05` | SMALLINT | NOT NULL |  |  |  |
| 49 | `USERFIELD06` | SMALLINT | NOT NULL |  |  |  |
| 50 | `USERFIELD07` | SMALLINT | NOT NULL |  |  |  |
| 51 | `USERFIELD08` | SMALLINT | NOT NULL |  |  |  |
| 52 | `USERFIELD09` | SMALLINT | NOT NULL |  |  |  |
| 53 | `USERFIELD10` | SMALLINT | NOT NULL |  |  |  |
| 54 | `PACKINGINSTRUCTIONS` | CLOB(1000000) |  |  |  |  |
| 55 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 56 | `CREATIONUSER` | CHAR(25) |  |  | audit | User who created the row (audit). |
| 57 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 58 | `LASTUPDATEUSER` | CHAR(25) |  |  | audit | User who last modified the row (audit). |
| 59 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 5

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `BIEMBROIDERY_BACKEMBROIDERY` | `COMPANYCODE`, `BACKEMBROIDERYCODE` | [`BIEMBROIDERY`](../OTHER/BIEMBROIDERY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BIEMBROIDERY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.BACKEMBROIDERYCODE = BIEMBROIDERY.CODE` |
| `BIEMBROIDERY_FRONTEMBROIDERY` | `COMPANYCODE`, `FRONTEMBROIDERYCODE` | [`BIEMBROIDERY`](../OTHER/BIEMBROIDERY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BIEMBROIDERY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.FRONTEMBROIDERYCODE = BIEMBROIDERY.CODE` |
| `BIEMBROIDERY_SLEEVEEMBROIDERY` | `COMPANYCODE`, `SLEEVEEMBROIDERYCODE` | [`BIEMBROIDERY`](../OTHER/BIEMBROIDERY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BIEMBROIDERY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.SLEEVEEMBROIDERYCODE = BIEMBROIDERY.CODE` |
| `BILAUNDRY_LAUNDRY` | `COMPANYCODE`, `LAUNDRYCODE` | [`BILAUNDRY`](../OTHER/BILAUNDRY.md) | `COMPANYCODE`, `CODE` | RESTRICT | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = BILAUNDRY.COMPANYCODE AND BICUSTOMEMBELLISHMENTS.LAUNDRYCODE = BILAUNDRY.CODE` |
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `BICUSTOMEMBELLISHMENTS.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `BICUSTOMEMBELLISHMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.TYPECODE,
       t.CODE,
       t.LONGDESCRIPTION,
       t.SHORTDESCRIPTION,
       t.SEARCHDESCRIPTION,
       t.FRONTDISCHARGE,
       t.FRONTPLASTISOL,
       t.FRONTDISTRESS,
       t.FRONTFOILPAPER,
       t.FRONTFLOCKING,
       t.FRONTGRAPHICSTYLENOTES
FROM   DB2ADMIN.BICUSTOMEMBELLISHMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
