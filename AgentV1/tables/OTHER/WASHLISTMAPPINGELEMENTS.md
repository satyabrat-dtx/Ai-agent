# DB2ADMIN.WASHLISTMAPPINGELEMENTS

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 25
- **Primary key**: `COMPANYCODE`, `DFFWASHINGLISTNO`, `NUMBERID`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`, `LOGICALWAREHOUSECODE`, `LOTCODE`, `CONTAINERITEMTYPECODE`, `CONTAINERSUBCODE01`, `CONTAINERELEMENTSCODE`, `ELEMENTSSUBCODEKEY`, `ELEMENTSCODE`, `PACKAGINGCODE`
- **FK degree**: referenced by 0 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 132413

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK FK | primary_key foreign_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `DFFWASHINGLISTNO` | CHAR(12) | NOT NULL | PK | primary_key |  |
| 2 | `NUMBERID` | DECIMAL(11,0) | NOT NULL | PK | primary_key |  |
| 3 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 4 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE02` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE03` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE04` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE05` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE06` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE07` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE08` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE09` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `SUBCODE10` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 14 | `LOGICALWAREHOUSECODE` | CHAR(8) | NOT NULL | PK | primary_key |  |
| 15 | `LOTCODE` | CHAR(35) | NOT NULL | PK | primary_key |  |
| 16 | `CONTAINERITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 17 | `CONTAINERSUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 18 | `CONTAINERELEMENTSCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 19 | `ELEMENTSSUBCODEKEY` | CHAR(20) | NOT NULL | PK | primary_key |  |
| 20 | `ELEMENTSCODE` | CHAR(15) | NOT NULL | PK | primary_key |  |
| 21 | `PACKAGINGCODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 22 | `UNIQUEID` | BIGINT | NOT NULL |  |  |  |
| 23 | `STATUSFLAG` | INTEGER | NOT NULL |  |  |  |
| 24 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `COMPANY_COMPANY` | `COMPANYCODE` | [`COMPANY`](../CORE_MASTER/COMPANY.md) | `CODE` | RESTRICT | `WASHLISTMAPPINGELEMENTS.COMPANYCODE = COMPANY.CODE` |

## Referenced by (child → this table) — 0

_None._

## Indexes

- `WASHLISTMAPPINGELEMENTSUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.DFFWASHINGLISTNO,
       t.NUMBERID,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08
FROM   DB2ADMIN.WASHLISTMAPPINGELEMENTS t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
