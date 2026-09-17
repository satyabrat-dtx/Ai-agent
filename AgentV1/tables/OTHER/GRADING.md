# DB2ADMIN.GRADING

- **Module**: `OTHER` (none confidence — no known prefix matched)
- **Roles**: `business_data`
- **Columns**: 24
- **Primary key**: `COMPANYCODE`, `ITEMTYPECODE`, `SUBCODE01`, `SUBCODE02`, `SUBCODE03`, `SUBCODE04`, `SUBCODE05`, `SUBCODE06`, `SUBCODE07`, `SUBCODE08`, `SUBCODE09`, `SUBCODE10`
- **FK degree**: referenced by 1 constraint(s), references 1 constraint(s)
- **Source**: `DB2ADMIN_DDL.sql` line 204662

## Columns

| # | Column | Type | Null | Key | Tags | Meaning |
|---|--------|------|------|-----|------|---------|
| 0 | `COMPANYCODE` | CHAR(3) | NOT NULL | PK | primary_key tenant_key | Company/legal-entity discriminator -- this schema's tenant key. Appears on 1,934 tables and is the leading primary-key column on most of them. Nearly every query should constrain it, and every join between company-scoped tables should include it. |
| 1 | `ITEMTYPECOMPANYCODE` | CHAR(3) | NOT NULL |  |  |  |
| 2 | `ITEMTYPECODE` | CHAR(3) | NOT NULL | PK | primary_key |  |
| 3 | `SUBCODE01` | CHAR(20) | NOT NULL | PK | primary_key generic_classification_code |  |
| 4 | `SUBCODE02` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 5 | `SUBCODE03` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 6 | `SUBCODE04` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 7 | `SUBCODE05` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 8 | `SUBCODE06` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 9 | `SUBCODE07` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 10 | `SUBCODE08` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 11 | `SUBCODE09` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 12 | `SUBCODE10` | CHAR(10) | NOT NULL | PK | primary_key generic_classification_code |  |
| 13 | `UOMCODE` | CHAR(3) |  | FK | foreign_key |  |
| 14 | `USERGENERICGROUPTYPECODE` | CHAR(3) |  |  |  |  |
| 15 | `STDSIZE` | CHAR(10) | NOT NULL |  |  |  |
| 16 | `TYPE` | CHAR(1) |  |  |  |  |
| 17 | `CREATIONDATETIME` | TIMESTAMP |  |  | audit | Local-time creation timestamp (audit). |
| 18 | `CREATIONUSER` | CHAR(50) |  |  | audit | User who created the row (audit). |
| 19 | `LASTUPDATEDATETIME` | TIMESTAMP |  |  | audit | Local-time last-modification timestamp (audit). |
| 20 | `LASTUPDATEUSER` | CHAR(50) |  |  | audit | User who last modified the row (audit). |
| 21 | `CREATIONDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC creation timestamp (audit). Prefer this over the local-time twin for comparisons across companies. |
| 22 | `LASTUPDATEDATETIMEUTC` | TIMESTAMP |  |  | audit | UTC last-modification timestamp (audit). |
| 23 | `ABSUNIQUEID` | BIGINT | NOT NULL |  | surrogate_id | Framework-assigned surrogate row id (BIGINT). Present on most tables. NO foreign key in this schema references it, but it is the target of the implicit FATHERID parent link. Not part of the primary key. |

## References (this table → parent) — 1

| Constraint | Local columns | → Table | → Columns | ON DELETE | JOIN predicate |
|---|---|---|---|---|---|
| `UNITOFMEASURE_UOM` | `UOMCODE` | [`UNITOFMEASURE`](../CORE_MASTER/UNITOFMEASURE.md) | `CODE` | RESTRICT | `GRADING.UOMCODE = UNITOFMEASURE.CODE` |

## Referenced by (child → this table) — 1

| Constraint | Child table | Child columns | JOIN predicate |
|---|---|---|---|
| `GRADING_LINE` | [`GRADINGDETAIL`](../OTHER/GRADINGDETAIL.md) | `GRADINGCOMPANYCODE`, `GRADINGITEMTYPECODE`, `GRADINGSUBCODE01`, `GRADINGSUBCODE02`, `GRADINGSUBCODE03`, `GRADINGSUBCODE04`, `GRADINGSUBCODE05`, `GRADINGSUBCODE06`, `GRADINGSUBCODE07`, `GRADINGSUBCODE08`, `GRADINGSUBCODE09`, `GRADINGSUBCODE10` | `GRADINGDETAIL.GRADINGCOMPANYCODE = GRADING.COMPANYCODE AND GRADINGDETAIL.GRADINGITEMTYPECODE = GRADING.ITEMTYPECODE AND GRADINGDETAIL.GRADINGSUBCODE01 = GRADING.SUBCODE01 AND GRADINGDETAIL.GRADINGSUBCODE02 = GRADING.SUBCODE02 AND GRADINGDETAIL.GRADINGSUBCODE03 = GRADING.SUBCODE03 AND GRADINGDETAIL.GRADINGSUBCODE04 = GRADING.SUBCODE04 AND GRADINGDETAIL.GRADINGSUBCODE05 = GRADING.SUBCODE05 AND GRADINGDETAIL.GRADINGSUBCODE06 = GRADING.SUBCODE06 AND GRADINGDETAIL.GRADINGSUBCODE07 = GRADING.SUBCODE07 AND GRADINGDETAIL.GRADINGSUBCODE08 = GRADING.SUBCODE08 AND GRADINGDETAIL.GRADINGSUBCODE09 = GRADING.SUBCODE09 AND GRADINGDETAIL.GRADINGSUBCODE10 = GRADING.SUBCODE10` |

## Indexes

- `GRADINGUID` (ABSUNIQUEID)

## Starter query

```sql
SELECT t.COMPANYCODE,
       t.ITEMTYPECOMPANYCODE,
       t.ITEMTYPECODE,
       t.SUBCODE01,
       t.SUBCODE02,
       t.SUBCODE03,
       t.SUBCODE04,
       t.SUBCODE05,
       t.SUBCODE06,
       t.SUBCODE07,
       t.SUBCODE08,
       t.SUBCODE09
FROM   DB2ADMIN.GRADING t
WHERE  t.COMPANYCODE = ?   -- tenant key: always constrain
FETCH FIRST 100 ROWS ONLY;
```
