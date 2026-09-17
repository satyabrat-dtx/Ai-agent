# DB2ADMIN.PDMAR4

- **Module**: `PDM` (medium confidence — table name starts with 'PDM')
- **Roles**: `business_data`
- **Columns**: 41
- **Primary key**: `COMPANYCODE`, `AZRECTYCODE`, `AZTPREC`, `AZCITEM`, `AZVERNR`, `AZVERST`, `AZCDSIZ`
- **FK degree**: referenced by 0 constraint(s), references 3 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 58878

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `AZRECTYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key |  |
| 2 | `AZTPREC` | DECIMAL(1,0) | NOT NULL | PK | primary_key |  |
| 3 | `AZCITEM` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 4 | `AZVERNR` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 5 | `AZVERST` | DECIMAL(3,0) | NOT NULL | PK | primary_key |  |
| 6 | `AZCDSIZ` | CHAR(10) | NOT NULL | PK | primary_key |  |
| 7 | `ITEMTYPECODE` | CHAR(3) |  | FK | foreign_key |  |
| 8 | `SUBCODE01` | CHAR(20) | NOT NULL |  | generic_classification_code |  |
| 9 | `SUBCODE02` | CHAR(10) |  |  | generic_classification_code |  |
| 10 | `SUBCODE03` | CHAR(10) |  |  | generic_classification_code |  |
| 11 | `SUBCODE04` | CHAR(10) |  |  | generic_classification_code |  |
| 12 | `SUBCODE05` | CHAR(10) |  |  | generic_classification_code |  |
| 13 | `SUBCODE06` | CHAR(10) |  |  | generic_classification_code |  |
| 14 | `SUBCODE07` | CHAR(10) |  |  | generic_classification_code |  |
| 15 | `SUBCODE08` | CHAR(10) |  |  | generic_classification_code |  |
| 16 | `SUBCODE09` | CHAR(10) |  |  | generic_classification_code |  |
| 17 | `SUBCODE10` | CHAR(10) |  |  | generic_classification_code |  |
| 18 | `AZMOLTI` | DECIMAL(7,2) |  |  |  |  |
| 19 | `AZFLUSE` | CHAR(1) |  |  |  |  |
| 20 | `AZPAKTY` | CHAR(10) |  |  |  |  |
| 21 | `AZ_PAKQY` | DECIMAL(9,0) |  |  |  |  |
| 22 | `AZDSC` | CHAR(50) |  |  |  |  |
| 23 | `AZANNUL` | CHAR(1) |  |  |  |  |
| 24 | `AZ_SIZID` | DECIMAL(5,0) |  |  |  |  |
| 25 | `AZRECTYCOMPANYCODE` | CHAR(3) | NOT NULL | FK | foreign_key |  |
| 26 | `ITEMTYPECOMPANYCODE` | CHAR(3) |  | FK | foreign_key |  |
| 27 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |
| 28 | `AZ_ALFA1` | CHAR(20) |  |  |  |  |
| 29 | `AZ_ALFA2` | CHAR(20) |  |  |  |  |
| 30 | `AZ_ALFA3` | CHAR(20) |  |  |  |  |
| 31 | `AZ_ALFA4` | CHAR(20) |  |  |  |  |
| 32 | `AZ_ALFA5` | CHAR(20) |  |  |  |  |
| 33 | `AZ_NUME1` | DECIMAL(29,9) |  |  |  |  |
| 34 | `AZ_NUME2` | DECIMAL(29,9) |  |  |  |  |
| 35 | `AZ_NUME3` | DECIMAL(29,9) |  |  |  |  |
| 36 | `AZ_NUME4` | DECIMAL(29,9) |  |  |  |  |
| 37 | `AZ_NUME5` | DECIMAL(29,9) |  |  |  |  |
| 38 | `AZ_FLSAM` | CHAR(1) |  |  |  |  |
| 39 | `AZ_PROPO` | DECIMAL(11,2) |  |  |  |  |
| 40 | `AZ_PERCE` | DECIMAL(11,2) |  |  |  |  |

## References (this table → parent) — 3

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `PDMAR4.COMPANYCODE = COMPANY.CODE` |
| `ITEMTYPE_AZRECTY` | `AZRECTYCOMPANYCODE`, `AZRECTYCODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PDMAR4.AZRECTYCOMPANYCODE = ITEMTYPE.COMPANYCODE AND PDMAR4.AZRECTYCODE = ITEMTYPE.CODE` |
| `ITEMTYPE_ITEMTYPE` | `ITEMTYPECOMPANYCODE`, `ITEMTYPECODE` | [`ITEMTYPE`](../CORE_MASTER/ITEMTYPE.md) | `COMPANYCODE`, `CODE` | RESTRICT | `PDMAR4.ITEMTYPECOMPANYCODE = ITEMTYPE.COMPANYCODE AND PDMAR4.ITEMTYPECODE = ITEMTYPE.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `PDMAR4UID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.AZRECTYCODE,
       t.AZTPREC,
       t.AZCITEM,
       t.AZVERNR,
       t.AZVERST,
       t.AZCDSIZ,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04
FROM   DB2ADMIN.PDMAR4 t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
